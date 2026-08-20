# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    stations = {}
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(";")
            if parts[0] == "Longitude":
                continue
            name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            stations[name] = (longitude, latitude)
    return stations


def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    return math.sqrt(x_km**2 + y_km**2)


def greatest_distance(stations: dict):
    greatest = 0
    best1 = ""
    best2 = ""
    for station1 in stations:
        for station2 in stations:
            if station1 != station2:
                d = distance(stations, station1, station2)
                if d > greatest:
                    greatest = d
                    best1 = station1
                    best2 = station2

    return best1, best2, greatest