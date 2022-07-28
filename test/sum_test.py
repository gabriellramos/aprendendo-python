"""
    Criar uma função soma e usar testes com pytest
"""
import pytest
import numbers 

def sum (a , b):
    if (isinstance(a, numbers.Number) and isinstance(b, numbers.Number)):
        return a + b
    else:
        return "Invalid input. Error. Please, input numbers type values."


def test_sum():
    assert sum(1,5) == 6


def test_validate_type_sum():
   assert isinstance(3, numbers.Number) and isinstance(5, numbers.Number) == True
    
def teste_sum3():
    assert sum('a','b') == "Invalid input. Error. Please, input numbers type values."

