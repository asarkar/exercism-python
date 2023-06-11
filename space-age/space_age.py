class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600.0

    def __init__(self, seconds: float) -> None:
        self.sec = seconds

    def on_earth(self):
        return self.__age(1.0)

    def on_mercury(self):
        return self.__age(0.2408467)

    def on_venus(self):
        return self.__age(0.61519726)

    def on_mars(self):
        return self.__age(1.8808158)

    def on_jupiter(self):
        return self.__age(11.862615)

    def on_saturn(self):
        return self.__age(29.447498)

    def on_uranus(self):
        return self.__age(84.016846)

    def on_neptune(self):
        return self.__age(164.79132)

    def __age(self, orbital_period: float) -> float:
        x = self.sec / (SpaceAge.EARTH_YEAR_SECONDS * orbital_period)
        return round(x, 2)
