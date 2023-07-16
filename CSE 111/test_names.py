from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    assert make_full_name("Joe", "Highland") == "Highland; Joe"
    assert make_full_name("Bob", "Smog") == "Smog; Bob"
    assert make_full_name("Bilbo", "Baggons") == "Baggons; Bilbo"


def test_extract_family_name():
    assert extract_family_name("Highland; Joe") == "Highland"
    assert extract_family_name("Smog; Bob") == "Smog"
    assert extract_family_name("Baggons; Bilbo") == "Baggons"


def test_extract_given_name():
    assert extract_given_name("Highland; Joe")  == "Joe"
    assert extract_given_name("Smog; Bob")  == "Bob"
    assert extract_given_name("Baggons; Bilbo")  == "Bilbo"



pytest.main(["-v", "--tb=line", "-rN", __file__])