import time


def database_call(query):
    time.sleep(5)
    return 1


def api_call():
    time.sleep(3)
    return 9


class Dataset:

    def __init__(self):
        self.data = None

    def load_data(self):
        time.sleep(4)
        self.data = 'slow data'