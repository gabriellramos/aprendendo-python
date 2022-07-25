"""
    Criar uma função soma e usar testes com pytest
"""

import pytest

def sum (a , b):
    return a + b


def test_sum():
    assert sum(1,5) == 6

def test_validate_type_sum():
    assert type(sum(3,1)) == int
    
def teste_sum3():
    assert sum('a','b') == "ab"