import pytest
import unittest.mock as mock
import mock_examples.simple_functions
from mock_examples.simple_functions import double


# note that I'm mocking the module when it is imported, not where CONSTANT_A is from
def test_mocking_constant_a(mocker):
    mocker.patch.object(mock_examples.simple_functions, 'CONSTANT_A', 2)
    expected = 4
    actual = double()

    assert expected == actual


def test_mocking_constant_a_again():
    expected = 2
    actual = double()

    assert expected == actual


def test_mocking_constant_a_one_more_time(mocker):
    mocker.patch.object(mock_examples.simple_functions, 'CONSTANT_A', 3)
    expected = 6
    actual = double()

    assert expected == actual


