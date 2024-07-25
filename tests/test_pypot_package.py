import pytest
import pypot_package.source as source

def test_sqrt():
    input = 4
    exp_output = 2.0
    output = source.sqrt(input)
    assert output == exp_output
    
def test_sqrt1():
    input = -4
    exp_output = complex(0,2)
    output = source.sqrt(input)
    assert output == pytest.approx(exp_output, rel=1e-6)
    