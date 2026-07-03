import time
from sensor import Sensor
from controller import Controller

sensor = Sensor()
controller = Controller()

print("===== Smart Egg Incubator =====")

while True:
    temp = sensor.read_temperature()
    hum = sensor.read_humidity()

    print("\nTemperature:", temp, "°C")
    print("Humidity:", hum, "%")

    print(controller.control_temperature(temp))
    print(controller.control_humidity(hum))

    time.sleep(3)