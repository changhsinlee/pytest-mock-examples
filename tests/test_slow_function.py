import pytest
from mock_examples.sample_script import slow_function


@pytest.mark.skip
def test_slow_function_super_slow():
    expected = 10
    actual = slow_function()
    assert expected == actual


def test_slow_function_mocked_database_call(mocker):
    mocker.patch(
        'mock_examples.sample_script.database_call',
        return_value=1
        )

    expected = 10
    # should take 5 seconds instead of 10
    actual = slow_function()
    assert expected == actual


def test_slow_function_mocked_database_api_call(mocker):
    mocker.patch(
        'mock_examples.sample_script.database_call',
        return_value=1
        )
    mocker.patch(
        'mock_examples.sample_script.api_call',
        return_value=9
    )

    expected = 10
    # should take 2 seconds instead of 10
    actual = slow_function
    assert expected == actual

