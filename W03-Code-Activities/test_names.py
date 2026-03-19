from names import make_full_name,extract_family_name,extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name("Matias","Martinez") == "Martinez; Matias"


def test_extract_family_name():

    assert extract_family_name("Diorio; Luna") == "Diorio"


def test_extract_given_name():

    assert extract_given_name("Martinez; Elias") == "Elias"
pytest.main(["-v","--tb=line","-rN",__file__])

