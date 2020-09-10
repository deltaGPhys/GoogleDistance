from views.location_logic import LocationWarehouse, TripWarehouse
from views.utils import FileFunctions


FileFunctions.file_stitcher("/Users/joshua.gates/Desktop/2019", "2019.json")


file = "/Users/joshua.gates/Desktop/2019/2019.json"

json = FileFunctions.open_json(file)

location_warehouse = LocationWarehouse()
location_warehouse.generate_location_list(json)
location_warehouse.show_locations()

print("\n***********************\n")

trip_warehouse = TripWarehouse()
trip_warehouse.generate_trip_list(json, location_warehouse)
trip_warehouse.show_trips()
trip_warehouse.save_csv(file[:-4]+"csv")

