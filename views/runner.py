from views.location_logic import LocationWarehouse, TripWarehouse
from views.utils import FileFunctions

json = FileFunctions.open_json("/Users/joshua.gates/Desktop/2019_FEBRUARY.json")
FileFunctions.print_primary_nodes(json)

location_warehouse = LocationWarehouse()
location_warehouse.generate_location_list(json)
location_warehouse.show_locations()

print("\n***********************\n")

trip_warehouse = TripWarehouse()
trip_warehouse.generate_trip_list(json, location_warehouse)
trip_warehouse.show_trips()

