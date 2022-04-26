import pytest
from isitwo import __version__
from isitwo.main import get_instance_name


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "input,expected",
    [
        ([{"Key": "Name", "Value": "banana"}], "banana"),
        ([{"Key": "Name", "Value": "pear"}, {"Key": "Foo", "Value": "Bar"}], "pear"),
        ([{"Key": "Name", "Value": "apple"}, {"Key": "Name", "Value": "Bar"}], "apple"),
        ([], ""),
    ],
)
def test_get_instance_name(input, expected):
    assert get_instance_name(input) == expected
