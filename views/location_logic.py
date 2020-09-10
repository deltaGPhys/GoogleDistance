import csv
import datetime
from typing import List

from models.models import Location, Trip
from views.utils import MathFunctions


class LocationWarehouse:

    locations: List[Location] = []

    def generate_location_list(self, input_json):
        for node in input_json:
            node_type = next(iter(node))
            try:
                if node_type == "placeVisit":
                    sub_node = node['placeVisit']
                    address = sub_node['location']['address']
                    name = sub_node['location']['name']
                    lat = MathFunctions.lat_fix(sub_node['location']['latitudeE7'])
                    long = MathFunctions.long_fix(sub_node['location']['longitudeE7'])
                    self.get_or_add_location(address, name, lat, long)
            except:
                print("bad location")

    def get_or_add_location(self, address: str, name: str, lat: int, long: int) -> Location:
        for loc in self.locations:
            if loc.address == address.replace("\n", " "):
                loc.lat = MathFunctions.lat_fix(lat)
                loc.long = MathFunctions.long_fix(long)
                return loc

        new_loc = Location(address=address.replace("\n", " "), name=name)
        new_loc.lat = MathFunctions.lat_fix(lat)
        new_loc.long = MathFunctions.long_fix(long)
        self.locations.append(new_loc)
        return new_loc

    def show_locations(self):
        for loc in self.locations:
            print(loc)

    def find_location(self, lat:int, long: int) -> Location:
        min_diff: float = 10000000000.0
        closest_location: Location = None

        for location in self.locations:
            diff: float = MathFunctions.calc_distance(lat, long, location.lat, location.long)
            if diff < min_diff:
                min_diff = diff
                closest_location = location

        # print(min_diff/10000000)
        return closest_location


class TripWarehouse:

    trips: List[Trip] = []
    start_date: datetime.date = datetime.datetime.strptime('01/01/2019', '%m/%d/%Y').date()
    end_date: datetime.date = datetime.datetime.strptime('01/01/2020', '%m/%d/%Y').date()

    def generate_trip_list(self, input_json, location_warehouse: LocationWarehouse):
        for node in input_json:
            node_type = next(iter(node))
            try:
                if node_type == "activitySegment" and node['activitySegment']['activityType'] == "IN_PASSENGER_VEHICLE":
                    sub_node = node['activitySegment']
                    start_lat = MathFunctions.lat_fix(sub_node['startLocation']['latitudeE7'])
                    start_long = MathFunctions.long_fix(sub_node['startLocation']['longitudeE7'])
                    end_lat = MathFunctions.lat_fix(sub_node['endLocation']['latitudeE7'])
                    end_long = MathFunctions.long_fix(sub_node['endLocation']['longitudeE7'])
                    distance = sub_node['distance']
                    date = sub_node['duration']['startTimestampMs']
                    trip = Trip(start_lat, start_long, end_lat, end_long, distance)

                    trip.start_location = location_warehouse.find_location(start_lat, start_long)
                    trip.end_location = location_warehouse.find_location(end_lat, end_long)
                    trip.date = date

                    if self.start_date <= trip.date <= self.end_date:
                        self.trips.append(trip)
            except:
                print("distance error")

    def show_trips(self):
        for trip in self.trips:
            print(trip)

    def save_csv(self, file: str):
        with open(file, mode='w') as output_file:
            trip_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for trip in self.trips:
                trip_writer.writerow([
                    trip.start_location.name,
                    trip.start_location.address,
                    trip.end_location.name,
                    trip.end_location.address,
                    trip.distance,
                    trip.date
                ])





