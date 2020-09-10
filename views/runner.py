from views.location_logic import FilterFunctions, LocationWarehouse
from views.utils import MathFunctions, FileFunctions

json = FileFunctions.open_json("/Users/joshua.gates/Desktop/2019_FEBRUARY.json")
FileFunctions.print_primary_nodes(json)

location_warehouse = LocationWarehouse()
location_warehouse.generate_location_list(json)
location_warehouse.show_locations()

