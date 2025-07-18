class Temperature:

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        if self._celsius is not None:
            return self._celsius
        else:
            raise ValueError("Celsius is None!")

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        self._celsius = None

    @property
    def fahrenheit(self):
        if self._celsius is not None:
            return (self._celsius * 9 / 5) + 32
        else:
            raise ValueError("Celsius is None!")

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

    @fahrenheit.deleter
    def fahrenheit(self):
        self._celsius = None

    @property
    def kelvin(self):
        if self._celsius is not None:
            return self._celsius + 273.15
        else:
            raise ValueError("Celsius is None!")

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = value - 273.15

    @kelvin.deleter
    def kelvin(self):
        self._celsius = None


t = Temperature(0)
print(t.fahrenheit)   # 32.0

t.kelvin = 300
print(round(t.celsius, 2))  # 26.85

del t.kelvin
print(t.celsius)      # Raises ValueError if you try to access t.fahrenheit
print(t.fahrenheit)   # Raises ValueError