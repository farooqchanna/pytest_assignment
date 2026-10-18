import pytest
from list_tool import find_max


def test_positive_numbers():
    assert find_max([2, 5, 8, 3]) == 8


def test_negative_numbers():
    assert find_max([-5, -2, -9, -1]) == -1


def test_single_item():
    assert find_max([7]) == 7


def test_empty_list_raises():
    with pytest.raises(ValueError):
        find_max([])


# Bonus: check the error message
def test_empty_list_error_message():
    with pytest.raises(ValueError, match="List is empty"):
        find_max([])