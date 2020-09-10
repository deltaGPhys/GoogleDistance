import json
from typing import List

from models.models import Location


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
            if loc.address == address:
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



