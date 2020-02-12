import time


class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):

        self.speed = 60

    def brake(self):
        time.sleep(5)
        self.speed = 0
