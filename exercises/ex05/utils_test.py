"""Test of List Utility Functions"""

__author__ = "730752527"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


# only_evens TESTS
def test_only_evens_expected_return() -> None:
    """Test for Expected Use Case"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_only_evens_no_mutation() -> None:
    """Tests that the original list is not mutated"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(test_list)
    assert test_list == [1, 2, 3, 4, 5, 6]


def test_only_evens_no_evens() -> None:
    """Tests with a list that has no evens"""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == []


# sub TESTS
def test_sub_expected_return() -> None:
    """Tests the expected use case"""
    test_list: list[int] = [7, 3, 0, 7, 5, 2, 5, 2, 7]
    assert sub(test_list, 5, 7) == [2, 5]


def test_sub_start_end_edge_cases() -> None:
    """Tests for when the start and end arguments are out of range"""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(test_list, -3, 20) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_no_mutation() -> None:
    """Test for if the function mutates the list"""
    test_list: list[int] = [1, 3, 4, 5]
    sub(test_list, 1, 2)
    assert test_list == [1, 3, 4, 5]


# add_at_index TESTS
def test_add_at_index_expected_mutation() -> None:
    """Tests for the expected mutation"""
    test_list: list[int] = [5, 4, 2, 1]
    add_at_index(test_list, 3, 2)
    assert test_list == [5, 4, 3, 2, 1]


def test_add_at_index_raises_error() -> None:
    """Tests that the function actually raises the error when needed"""
    test_list: list[int] = [3, 4, 3, 7, 3, 5]
    with pytest.raises(IndexError):
        add_at_index(test_list, -2, 10)


def test_add_at_index_return_nothing() -> None:
    """Tests if the function returns nothing"""
    test_list: list[int] = [4, 3, 2, 4, 6]
    assert add_at_index(test_list, 3, 3) is None
