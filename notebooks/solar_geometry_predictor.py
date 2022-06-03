import math


class SolarGeometryPredictor:
    def __init__(self, latitude, day_number, hour):
        self.latitude = latitude
        self.day_number = day_number
        self.hour = hour
        self.hour_angle = 0.0
        self.solar_declination = 0.0
        self.solar_altitude = 0.0
        self.solar_azimuth = 0.0

    def predict(self):
        self.solar_declination = self.calculate_solar_declination(self.day_number)
        self.hour_angle = self.calculate_hour_angle(self.calculate_hours_after_local_noon(self.hour))
        self.solar_altitude = self.calculate_solar_altitude(self.latitude, self.solar_declination, self.hour_angle)
        self.solar_azimuth = self.calculate_solar_azimuth(self.solar_altitude, self.solar_declination, self.hour_angle)

    @staticmethod
    def calculate_hours_after_local_noon(hour):
        return hour - 12.0

    @staticmethod
    def calculate_hour_angle(hours_after_local_noon):
        return 0.25 * (hours_after_local_noon * 60.0)

    @staticmethod
    def calculate_solar_declination(day_number):
        return 23.45 * math.sin((360.0 * (284.0 + day_number) / 365.0) * math.pi / 180.0)

    @staticmethod
    def calculate_solar_altitude(latitude, solar_declination, hour_angle):
        radian_latitude = latitude * math.pi / 180.0
        radian_hour_angle = hour_angle * math.pi / 180.0
        radian_solar_declination = solar_declination * math.pi / 180.0

        radians = math.asin((math.sin(radian_latitude) * math.sin(radian_solar_declination) +
                             math.cos(radian_latitude) * math.cos(radian_solar_declination) *
                             math.cos(radian_hour_angle)))

        return radians * 180.0 / math.pi

    @staticmethod
    def calculate_solar_azimuth(solar_altitude, solar_declination, hour_angle):
        radian_solar_altitude = solar_altitude * math.pi / 180.0
        radian_solar_declination = solar_declination * math.pi / 180.0
        radian_hour_angle = hour_angle * math.pi / 180.0

        return (math.asin((math.cos(radian_solar_declination) *
                           math.sin(radian_hour_angle)) / math.cos(radian_solar_altitude))) * 180.0 / math.pi
