class Controller:
    def control_temperature(self, temperature):
        if temperature < 37.5:
            return "Heater ON"
        elif temperature > 38.5:
            return "Cooler ON"
        else:
            return "Temperature Stable"

    def control_humidity(self, humidity):
        if humidity < 55:
            return "Humidifier ON"
        elif humidity > 65:
            return "Fan ON"
        else:
            return "Humidity Stable"