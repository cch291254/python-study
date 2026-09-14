import pytest
def calculate_salary(base,bonus):
    if base<0:
        raise ValueError("基本工资不能为负数")
    return base+bonus


def test_calculate_salary():
    result = calculate_salary(8000, 2000)
    assert result == 10000
def test_no_bonus():
    result = calculate_salary(8000, 0)
    assert result == 8000


def test_salary_deduction():
    result = calculate_salary(8000, -500)
    assert result == 7500









def test_negative_base():
    with pytest.raises(ValueError):
        calculate_salary(-8000,2000)
    

