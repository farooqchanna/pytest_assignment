import pytest
from mymath import is_leap_year


@pytest.mark.parametrize("year, expected", [
    (2024, True),
    (2023, False),
    (1900, False),
    (2000, True),
])
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected