import sys 
import os 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import model 

def test_add():
    assert model.add(1, 4) == 5
    assert model.add(4, 4) == 8
    assert model.add(1, 9) == 10
    assert model.add(9, 4) == 13

def test_mult(): 
    assert model.mult(2, 3) == 6
    assert model.mult(4, 5) == 20