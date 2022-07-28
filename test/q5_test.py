import pytest
import numbers
#from ..list4.q5 import five_part
#from ..list4 import q5
#resolver

def five_part(num):
    if (isinstance(num, numbers.Number)):
        return num/5.0
    else:
        return "Nao eh um numero"

# erro ao importar
def test_five_part_int():
    assert five_part(25) == 5

def test_five_part_success():
    assert five_part(10.12546) == 2.025092

def test_five_part_only_numbers():
    assert five_part("1") == "Nao eh um numero"
