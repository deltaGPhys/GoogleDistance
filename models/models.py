from statistics import mean
from typing import List

from views.utils import MathFunctions


class Location:

    def __init__(self, address: str, name: str):
        self.name: str = name
        self.address: str = address
        self._lat: int = 0
        self._long: int = 0
        self.lat_set: List[int] = []
        self.long_set: List[int] = []

    @property
    def lat(self) -> int:
        return self._lat

    @lat.setter
    def lat(self, new_lat: int):
        self.lat_set.append(new_lat)
        self._lat = round(mean(x for x in self.lat_set))

    @property
    def long(self) -> int:
        return self._long

    @long.setter
    def long(self, new_long: int):
        self.long_set.append(new_long)
        self._long = round(mean(x for x in self.long_set))

    def isSame(self, location):
        return MathFunctions.calc_pct_diff(self.lat, location.lat) < .01 and MathFunctions.calc_pct_diff(self.long, location.long) < .01

    def __str__(self):
        return f'{self.name.rstrip() or "<None>"} ({self.address or "<None>"}) <{self.lat}/{self.long}>'


class ActivitySegment:

    def __init__(self, start_location: Location, end_location: Location, distance: int):
        self.start_location = start_location
        self.end_location = end_location
        self.distance: float = distance/1609.34
