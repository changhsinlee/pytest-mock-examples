from mock_examples.slow import api_call, Dataset


def slow_function():
    api_result = api_call()
    # do some more stuff here
    return api_result


def slow_dataset():
    dataset = Dataset()
    dataset.load_data()
    return dataset.data
