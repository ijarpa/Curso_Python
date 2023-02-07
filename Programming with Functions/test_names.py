from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Ivan", "Jarpa") == "Jarpa; Ivan"

def test_extract_family_name():
    assert extract_family_name("Jarpa; Ivan") == "Jarpa"

def test_extract_given_name():
    assert extract_given_name("Jarpa; Ivan") == "Ivan"

pytest.main(["-v", "--tb=line", "-rN", __file__])