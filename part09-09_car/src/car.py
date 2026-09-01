# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0
    
    def fill_up(self):
        self.__petrol = 60

    def drive(self, km: int):
        actual_km = min(km, self.__petrol)
        self.__petrol -= actual_km
        self.__odometer += actual_km


    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"