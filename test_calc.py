"""
tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert calculator.add(2, 3) == 5

    def test_subtract(self):
        assert calculator.sub(8, 3) == 5

    def test_multiply(self):
        assert calculator.mult(2, 3) == 6

    def test_devide(self):
        assert calculator.div(10, 5) == 2
