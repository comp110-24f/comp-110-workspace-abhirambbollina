__author__ = "730752527"

# import pytest
from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_expected_value() -> None:
    """Tests that the function returns the correct value"""
    test_list = [1, 3, 4, 7, 9, 3]
    assert find_and_remove_max(test_list) == 9


def test_find_and_remove_max_expected_mutation() -> None:
    """Tests that the function mutates the list correctly"""
    test_list = [6, 8, 4, 2, 8, 3, 8]
    find_and_remove_max(test_list)
    assert test_list == [6, 4, 2, 3]


def test_find_and_remove_max_empty_list() -> None:
    """Edge Case: Tests if the function aftually returns -1 for an empty list"""
    test_list = []
    assert find_and_remove_max(test_list) == -1
