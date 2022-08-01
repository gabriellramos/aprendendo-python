import pytest
import sys
import os
# adding Folder_2 to the system path
sys.path.append(os.path.join('C:/', 'Users', 'gabri', 'OneDrive', 'Documents', 'GitHub', 'aprendendo-python', 'q5'))

# importing the add and odd_even
# function
from q5 import five_part
#resolver

# erro ao importar
def test_five_part_int():
    assert five_part(25) == 5

def test_five_part_success():
    assert five_part(10.12546) == 2.025092

def test_five_part_only_numbers():
    assert five_part("1") == 0.0
