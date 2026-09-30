# Cmput 455 sample code
# Expected value (EV) for discrete probabilities and values
# Written by Martin Mueller

from typing import List, Tuple, Callable
from operator import mul
from math import isclose

Probabilities = List[float]
DiceValues = List[int]
Results = Tuple[Probabilities, DiceValues]

def abs_close(a: float, b: float) -> bool:
    return isclose(a, b, abs_tol=1e-8)

def ev(prob: list[float], values: list[int]) -> float:
    return sum(map(mul, prob, values), 0.0)

ExampleFunc = Callable[[], Results]

def example1() -> Results:
    prob: Probabilities = 6 * [1 / 6]
    values: DiceValues = [i for i in range(1, (6 + 1))]
    return prob, values

def example2() -> Results:
    p_6: float = 0.3
    p_other: float = (1 - p_6) / (6 - 1)
    prob: Probabilities = 5 * [p_other] + [p_6]
    values: DiceValues = [i for i in range(1, (6 + 1))]
    return prob, values

def example3() -> Results:
    num_sides = 1000
    prob: Probabilities = num_sides * [1 / num_sides]
    values: DiceValues = [i for i in range(1, (num_sides + 1))]
    return prob, values

def test_ev(example: ExampleFunc, correct_pv: float) -> None:
    prob: Probabilities
    values: DiceValues
    prob, values = example()
    assert abs_close(ev(prob, values), correct_pv)

def test_ev_all() -> None:
    tests = [(example1, 3.5),
             (example2, 3.9),
             (example3, (1000.0 + 1)/2),
            ]
    for (e,c) in tests:
        test_ev(e,c)


if __name__ == "__main__":
    print()
    print("=== Example 1: Six-sided fair die ===")
    prob: Probabilities
    values: DiceValues
    prob, values = example1()
    print(f"EV for fair die = {ev(prob, values):.3f}\n")

    print("=== Example 2: unfair (loaded) die ===")
    prob, values = example2()
    print(f"EV for unfair die = {ev(prob, values):.3f}\n")

    print("=== Example 3: 1000-sided fair die ===")
    prob, values = example3()
    print(f"EV for 1000-sided fair die = {ev(prob, values):.3f}\n")

    test_ev_all()