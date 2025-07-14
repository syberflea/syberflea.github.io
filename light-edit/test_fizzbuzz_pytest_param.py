import pytest
# Assuming fizzbuzz is defined in 'your_module.py'
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize(
    "input,expected",
    [
        (30, "fizz buzz"),  # Divisible by 15
        (9, "fizz"),  # Divisible by 3
        (10, "buzz"),  # Divisible by 5
        (4, 4),  # Not divisible by 3 or 5
        (0, "fizz buzz"),  # Edge case: 0 (divisible by 15)
        (33, "fizz"),  # Additional case: Divisible by 3
        (55, "buzz"),  # Additional case: Divisible by 5
        (98, 98),  # Additional case: Not divisible by 3 or 5
    ],
)
def test_fizzbuzz(input, expected):
    assert (
           fizzbuzz(input) == expected
    ), f"Expected {expected} for input {input}"