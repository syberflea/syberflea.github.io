import pytest
from fizzbuzz import fizzbuzz

def test_fizzbuzz_multiple_of_both():
    assert fizzbuzz(15) == "fizz buzz"
    assert fizzbuzz(30) == "fizz buzz"
    assert fizzbuzz(45) == "fizz buzz"

def test_fizzbuzz_multiple_of_three():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(6) == "fizz"
    assert fizzbuzz(9) == "fizz"

def test_fizzbuzz_multiple_of_five():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(20) == "buzz"

def test_fizzbuzz_not_multiple_of_three_or_five():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(7) == 7
    assert fizzbuzz(11) == 11