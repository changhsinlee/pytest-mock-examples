from mock_examples.car import Car


def test_mocking_brake():
    car = Car()
    car.accelerate()
    assert car.speed == 60
    car.brake()
    assert car.speed == 0


def test_mocking_brake_patched(mocker):
    def instant_brake(self):
        self.speed = 10

    car = Car()
    car.accelerate()
    assert car.speed == 60
    mocker.patch.object(Car, 'brake', instant_brake)
    car.brake()
    assert car.speed == 10
