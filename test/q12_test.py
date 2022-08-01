import pytest
import sys
import os
# adding Folder_2 to the system path
sys.path.append(os.path.join('C:/', 'Users', 'gabri', 'OneDrive', 'Documents', 'GitHub', 'aprendendo-python', 'q5'))

# importing the add and odd_even
# function
from q12 import soma_algarismos

def test_soma_algarismos():
    assert soma_algarismos(251) == 8