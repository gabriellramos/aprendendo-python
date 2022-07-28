import pytest
from list4 import Q5
# erro ao importar
def test_five_part_incorrect():
    assert five_part(10.12546) == 5

def test_five_part_success():
    assert five_part(10.12546) == 2.025092

def test_five_part_only_numbers():
    assert five_part("1") == "Nao eh um numero"

print(dir())