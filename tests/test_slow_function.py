import pytest
from mock_examples.main import slow_function


@pytest.mark.skip
def test_slow_function_super_slow():
    expected = 9
    actual = slow_function()
    assert expected == actual


@pytest.fixture(autouse=True)
def test_slow_function_mocked_api_call(mocker, expected):
    mocker.patch(
        'mock_examples.main.api_call',
        return_value=expected
    )

@pytest.mark.parametrize(
    "expected",
    [(7), (2)],
)
def test_slow_function_mocked_api_call_pm(expected):
    actual = slow_function()
    assert expected == actual