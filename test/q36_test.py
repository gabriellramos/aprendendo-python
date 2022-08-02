import pytest
import sys
import os
# adding Folder_2 to the system path
sys.path.append(os.path.join('C:/', 'Users', 'gabri', 'OneDrive', 'Documents', 'GitHub', 'aprendendo-python', 'q5'))

# importing the add and odd_even
# function
from q36 import sf

def test_sf():
    assert sf(4) == 288