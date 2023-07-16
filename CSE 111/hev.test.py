from hev import main, electrical_vehicles
import pytest

def test_man():
    assert main("Toyota", "Prius") == "Prius"; "Toyota"



def test_electrical_vehicles():
    assert electrical_vehicles("filename", "text_file") == "text_file"; "filename"


pytest.main(["-v", "--tb=line", "-rN", __file__])