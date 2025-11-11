import pytest
from logic import isEven


class TestIsEven:
    def test_positive_even_number(self):
        assert isEven(2) is True
        assert isEven(4) is True
        assert isEven(100) is True

    def test_positive_odd_number(self):
        assert isEven(1) is False
        assert isEven(3) is False
        assert isEven(99) is False

    def test_negative_even_number(self):
        assert isEven(-2) is True
        assert isEven(-4) is True
        assert isEven(-100) is True

    def test_negative_odd_number(self):
        assert isEven(-1) is False
        assert isEven(-3) is False
        assert isEven(-99) is False

    def test_zero(self):
        assert isEven(0) is True

    def test_large_even_number(self):
        assert isEven(1000000) is True

    def test_large_odd_number(self):
        assert isEven(1000001) is False
