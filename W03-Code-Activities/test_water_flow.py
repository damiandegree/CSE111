from water_flow import water_column_height,pressure_gain_from_water_height,pressure_loss_from_pipe,pressure_loss_from_fittings,reynolds_number,pressure_loss_from_pipe_reduction
from pytest import approx
import pytest

def test_water_column_height():

    assert water_column_height(0.0,0.0) == approx(0,abs=0.01)
    assert water_column_height(0.0,10.0) == approx(7.5,abs=0.01)
    assert water_column_height(25.0,0.0) == approx(25.0,abs=0.01)
    assert water_column_height(48.3,12.8) == approx(57.9,abs=0.01)
    
def test_pressure_gain_from_water_height():

    assert pressure_gain_from_water_height() == approx(,abs=0.001)
    assert pressure_gain_from_water_height() == approx(,abs=0.001)
    assert pressure_gain_from_water_height() == approx(,abs=0.001)

    pass
def test_pressure_loss_from_pipe():
    pass
def test_pressure_loss_from_fittings():
    pass
def test_reynolds_number():
    pass
def test_pressure_loss_from_pipe_reduction():
    pass


pytest.main(["-v","--tb=line","-rN",__file__])