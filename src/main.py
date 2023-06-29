import location
import jsonConverter

location_list: list = []
# library Lothstr.
library_H_ap_list = ["apa02-4rh", "apa04-3rh", "apa05-2rh", "apa05-3rh", "apa06-2rh", "apa06-3rh", "apa07-2rh"]
location_list.append(location.location("Bibliothek_H_Bau", "rh", 430, library_H_ap_list))
location_list.append(location.location("Bibliothek_I_Bau", "ri", 250))
# library Pasing
location_list.append(location.location("Bibliothek_L_Bau", "rl", 200, ["apa14-1rl", "apa15-1rl"]))
# Cafeteria Karlstr.
location_list.append(location.location("Cafeteria_Karlstr.", "rf", 100, ["apa06-4rf"]))
# mensa's
location_list.append(
    location.location("Mensa_Lothstr.", "rh", 280, ["apa02-1rh", "apa03-1rh", "apa05-0rh", "apa06-0rh"]))

location_list.append(location.location("Mensa_Pasing", "rl", 120, ["apa15-0rl", "apa18-0rl"]))

for location in location_list:
    jsonConverter.json_creator(location, location.name)
jsonConverter.json_creator(location_list, "combined")
