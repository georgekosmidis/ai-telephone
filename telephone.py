import os
import re
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent
BASIS = ROOT / "basis.py"
OUT_DIR = ROOT / "generations"
SYSTEM_PROMPT = "Improve the following Python code. Return nothing but the improved code. Do not add comments. Pure code only."
CODE_BLOCK = re.compile(r"```(?:python|py)?\s*\n(.*?)```", re.DOTALL)


def extract_code(text: str) -> str:
    match = CODE_BLOCK.search(text)
    return match.group(1) if match else text


def build_prompt(source: Path) -> str:
    return f"```python\n{source.read_text(encoding='utf-8')}\n```"


def main() -> None:
    load_dotenv(ROOT / ".env")
    endpoint = os.environ["AZURE_AI_ENDPOINT"]
    key = os.environ["AZURE_AI_KEY"]
    model = os.environ["AZURE_AI_STORY_DEPLOYMENT"]
    generations = int(os.environ["GENERATIONS"])

    client = Anthropic(base_url=f"{endpoint}/anthropic", api_key=key)
    OUT_DIR.mkdir(exist_ok=True)

    last = max((int(p.stem) for p in OUT_DIR.glob("*.py")), default=0)
    source = OUT_DIR / f"{last}.py" if last else BASIS
    for gen in range(last + 1, generations + 1):
        response = client.messages.create(
            model=model,
            max_tokens=16000,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": build_prompt(source)}],
        )
        target = OUT_DIR / f"{gen}.py"
        text = "".join(block.text for block in response.content if block.type == "text")
        target.write_text(extract_code(text), encoding="utf-8")
        print(f"[{gen}/{generations}] {source.name} -> {target.name}")
        source = target


if __name__ == "__main__":
    main()
