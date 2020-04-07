import time

from mock_examples.slow import database_call, api_call, Dataset


def useful_computation(*args):
    time.sleep(2)
    return sum(args)


def slow_function():
    query_result1 = database_call('some select query')
    api_result = api_call()

    # should return 1 + 9 = 10
    output = useful_computation(query_result1, api_result)
    return output


def slow_dataset():
    dataset = Dataset()
    dataset.load_data()
    return dataset.data
