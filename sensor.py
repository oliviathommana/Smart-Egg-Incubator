import random

class Sensor:
    def read_temperature(self):
        return round(random.uniform(35.0, 39.5), 1)

    def read_humidity(self):
        return round(random.uniform(45.0, 70.0), 1)