import pytest
from mock_examples.main import slow_function, slow_dataset


# @pytest.mark.skip
def test_slow_function_super_slow():
    expected = 10
    actual = slow_function()
    assert expected == actual


def test_slow_function_mocked_database_call(mocker):
    # 5 (database call) + 9 (api call) = 14
    mocker.patch(
        'mock_examples.main.database_call',
        return_value=5
        )

    expected = 14
    # should take 5 seconds instead of 10
    actual = slow_function()
    assert expected == actual


def test_slow_function_mocked_database_api_call(mocker):
    # 1 (database call) + 9 (api call) = 10
    mocker.patch(
        'mock_examples.main.database_call',
        return_value=1
        )
    mocker.patch(
        'mock_examples.main.api_call',
        return_value=9
    )

    expected = 10
    # should take 2 seconds instead of 10
    actual = slow_function()
    assert expected == actual


def test_mocking_class_method(mocker):
    expected = 'xyz'

    def mock_load(self):
        self.data = 'xyz'

    mocker.patch(
        'mock_examples.main.Dataset.load_data',
        mock_load
    )
    actual = slow_dataset()
    assert expected == actual
