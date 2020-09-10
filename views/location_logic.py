import json
from typing import List

from models.models import Location, Trip
from views.utils import MathFunctions


class FilterFunctions:

    @staticmethod
    def filter_travel_methods(method: str, data):
        """ Filter out all but desired travel method

        :param method: the string representing the desired method to keep
        :param data: json to be filtered
        :return: json
        """

        filtered_json = {}

        for node in json:
            node_type = next(iter(node))
            # if node_type == "placeVisit" or node_type == "activitySegment" and node["duration"]["activityType"]

        return None


class LocationWarehouse:

    locations: List[Location] = []

    def generate_location_list(self, input_json):
        for node in input_json:
            node_type = next(iter(node))
            if node_type == "placeVisit":
                sub_node = node['placeVisit']
                address = sub_node['location']['address']
                name = sub_node['location']['name']
                lat = sub_node['location']['latitudeE7']
                long = sub_node['location']['longitudeE7']
                self.get_or_add_location(address, name, lat, long)

    def get_or_add_location(self, address: str, name: str, lat: int, long: int) -> Location:
        for loc in self.locations:
            if loc.address == address.replace("\n", " "):
                loc.lat = lat
                loc.long = long
                return loc

        new_loc = Location(address=address.replace("\n", " "), name=name)
        new_loc.lat = lat
        new_loc.long = long
        self.locations.append(new_loc)
        return new_loc

    def show_locations(self):
        for loc in self.locations:
            print(loc)

    def find_location(self, lat:int, long: int) -> Location:
        min_diff: float = 10000000000.0
        closest_location: Location = None

        for location in self.locations:
            diff: float = MathFunctions.calc_distance(lat, location.lat, long, location.long)
            if diff < min_diff:
                min_diff = diff
                closest_location = location

        print(min_diff)
        return closest_location


class TripWarehouse:

    trips: List[Trip] = []

    def generate_trip_list(self, input_json, location_warehouse: LocationWarehouse):
        for node in input_json:
            node_type = next(iter(node))
            if node_type == "activitySegment" and node['activitySegment']['duration']['activityType'] == "IN_PASSENGER_VEHICLE":
                sub_node = node['activitySegment']
                start_lat = sub_node['startLocation']['latitudeE7']
                start_long = sub_node['startLocation']['longitudeE7']
                end_lat = sub_node['endLocation']['latitudeE7']
                end_long = sub_node['endLocation']['longitudeE7']
                distance = sub_node['duration']['distance']
                trip = Trip(start_lat, start_long, end_lat, end_long, distance)

                trip.start_location = location_warehouse.find_location(start_lat, start_long)
                trip.end_location = location_warehouse.find_location(end_lat, end_long)
                self.trips.append(trip)

    def show_trips(self):
        for trip in self.trips:
            print(trip)




