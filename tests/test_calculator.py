"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8 

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected


    def test_add_invalid_input(self, calc):
        """Test adding invalid inputs raises InvalidInputException."""
        with pytest.raises(InvalidInputException, match="outside the valid range"):
            calc.add(1000000, 1)

        with pytest.raises(InvalidInputException):
            calc.add(-1000000, 1)

        with pytest.raises(InvalidInputException):
            calc.add(1, -1000000)
        

    def test_values_is_allowed_add(self, calc):
        assert calc.add(999999, 0) == 999999
    def test_values_is_allowed_add_2(self, calc):
        assert calc.add(0, -999999) == -999999
        


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_invalid_input_raises(self, calc):
        with pytest.raises(InvalidInputException):
            calc.subtract(1000000, 0)
        with pytest.raises(InvalidInputException):
            calc.subtract(0, 1000000)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 15
        # Act
        result = calc.multiply(a, b)
        # Assert
        assert result == expected

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(123, 0) == 0

    def test_multiply_negative(self, calc):
        assert calc.multiply(-2, 3) == -6

    def test_multiply_invalid_input_raises(self, calc):
        with pytest.raises(InvalidInputException):
            calc.multiply(1000000, 1)
        with pytest.raises(InvalidInputException):
            calc.multiply(1, 1000000)
    


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 3
        expected = 2
        # Act
        result = calc.divide(a, b)
        # Assert
        assert result == expected

    def test_divide_by_zero(self, calc):
        """Test dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(5, 0)
    
    def test_divide_zero(self, calc):
        assert calc.divide(0, 5) == 0

    def test_divide_non_integer_result(self, calc):
        assert calc.divide(5, 2) == 2.5

    def test_divide_negative_non_integer_result(self, calc):
        assert calc.divide(1, -2) == -0.5

    def test_divide_invalid_input_raises(self, calc):
        with pytest.raises(InvalidInputException):
            calc.divide(1000000, 1)
        with pytest.raises(InvalidInputException):
            calc.divide(1, 1000000)

