import pytest
from warnings import catch_warnings
from main import to_infix_notation

#проверка корректных выражений
def test_to_infix_notation_valid_1():
    expression = "* + 3 4 5"
    expected = "(3 + 4) * 5"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_valid_2():
    expression = "- 8 / 4 2"
    expected = "8 - (4 / 2)"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_valid_3():
    expression = "+ 10 * 2 3"
    expected = "10 + (2 * 3)"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_valid_4():
    expression = "/ - 20 5 3"
    expected = "(20 - 5) / 3"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_valid_5():
    expression = "+ * 1 1 1"
    expected = "(1 * 1) + 1"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_valid_6():
    expression = "- / 100 5 10"
    expected = "(100 / 5) - 10"
    assert to_infix_notation(expression) == expected

#проверка выражений с недостатком операндов
def test_to_infix_notation_not_enough_operands_1():
    expression = "* + 1 2"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert result == ""
        assert any("Not enough operands" in str(w.message) for w in warnings)

def test_to_infix_notation_not_enough_operands_2():
    expression = "- 9"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert result == ""
        assert any("Not enough operands" in str(w.message) for w in warnings)

def test_to_infix_notation_not_enough_operands_3():
    expression = "+ * 6 7"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert result == ""
        assert any("Not enough operands" in str(w.message) for w in warnings)

def test_to_infix_notation_not_enough_operands_4():
    expression = "* - 3"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert result == ""
        assert any("Not enough operands" in str(w.message) for w in warnings)

#проверка выражений с лишними операндами
def test_to_infix_notation_extra_operands_1():
    expression = "/ + 5 3 4 8"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert "extra operands" in str(warnings[-1].message) if warnings else False

def test_to_infix_notation_extra_operands_2():
    expression = "- 6 + 4 3 9"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert "extra operands" in str(warnings[-1].message) if warnings else False

def test_to_infix_notation_extra_operands_3():
    expression = "* + 5 4 3 2"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert "extra operands" in str(warnings[-1].message) if warnings else False

def test_to_infix_notation_extra_operands_4():
    expression = "- 10 * 5 2 3"
    with catch_warnings(record=True) as warnings:
        result = to_infix_notation(expression)
        assert "extra operands" in str(warnings[-1].message) if warnings else False

#проверка пустого ввода
def test_to_infix_notation_empty():
    assert to_infix_notation("") == ""

# Тпроверка сложных выражений
def test_to_infix_notation_complex_1():
    expression = "* + 1 2 + 3 4"
    expected = "(1 + 2) * (3 + 4)"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_complex_2():
    expression = "- + 5 3 * 2 2"
    expected = "(5 + 3) - (2 * 2)"
    assert to_infix_notation(expression) == expected

def test_to_infix_notation_complex_3():
    expression = "* + 12 4 - 5 11"
    expected = "(12 + 4) * (5 - 11)"
    assert to_infix_notation(expression) == expected
