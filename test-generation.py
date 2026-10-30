import importlib.util
import itertools
import random
from pathlib import Path

ROOT = Path(__file__).parent
BASIS = ROOT / "basis.py"
OUT_DIR = ROOT / "generations"


def build_cases() -> list[list]:
    cases: list[list] = [
        [],
        [1],
        [2, 2, 2, 2],
        list(range(20)),
        list(range(20, 0, -1)),
        [-3, 0, -1, 5, -10, 2],
        [1.5, -0.5, 3.25, 0.0, 2.75],
        ["pear", "apple", "fig", "banana"],
    ]
    for n in range(7):
        cases.extend(list(p) for p in itertools.permutations(range(n)))
    rng = random.Random(0)
    for _ in range(500):
        cases.append([rng.randint(-10, 10) for _ in range(rng.randint(0, 40))])
    return cases


def load(path: Path):
    spec = importlib.util.spec_from_file_location(f"gen_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.bubble_sort


def error_rate(bubble_sort, cases: list[list]) -> float:
    failures = sum(bubble_sort(list(case)) != sorted(case) for case in cases)
    return failures / len(cases)


def main() -> None:
    cases = build_cases()
    paths = [BASIS] + sorted(OUT_DIR.glob("*.py"), key=lambda p: int(p.stem))
    rates = [error_rate(load(path), cases) for path in paths]
    print(f"{len(cases)} test cases per generation\n")
    for gen, (path, rate) in enumerate(zip(paths, rates)):
        print(f"{gen:>3}  {path.name:<10} {rate:7.2%}")
    failing = [gen for gen, rate in enumerate(rates) if rate]
    print(f"\nFailing generations: {failing}")


if __name__ == "__main__":
    main()
