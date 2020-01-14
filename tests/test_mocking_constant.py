import pytest
import unittest.mock as mock

from mock_examples.simple_functions import double


# note that I'm mocking the module when it is imported, not where CONSTANT_A is from
@mock.patch('mock_examples.simple_functions.double.CONSTANT_A', 2)
def test_mocking_constant_a():
    expected = 4
    actual = double()

    assert expected == actual


def test_mocking_constant_a_again():
    expected = 2
    actual = double()

    assert expected == actual


@mock.patch('mock_examples.simple_functions.CONSTANT_A', 3)
def test_mocking_constant_a_one_more_time():
    expected = 6
    actual = double()

    assert expected == actual
