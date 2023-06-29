import parser
import location
import jsonpickle

location_list: list = []
max_seen_clients = {
    "Bibliothek H Bau": 0,
    "Bibliothek I Bau": 302,
    "Bibliothek L Bau": 0,
    "Cafeteria Karlstr.": 0,
    "Mensa Lothstr.": 0,
    "Mensa Pasing": 0
    # todo calculate max value
}
# library Lothstr.
library_H_ap_list = ["apa02-4rh", "apa04-3rh", "apa05-2rh", "apa05-3rh", "apa06-2rh", "apa06-3rh", "apa07-2rh"]
location_list.append(location.location("Bibliothek H Bau", "rh", library_H_ap_list))
location_list.append(location.location("Bibliothek I Bau", "rh"))
# library Pasing
location_list.append(location.location("Bibliothek L Bau", "rl", ["apa14-1rl", "apa15-1rl"]))
# Cafeteria Karlstr.
location_list.append(location.location("Cafeteria Karlstr.", "rf", ["apa06-4rf"]))
# mensa's
location_list.append(location.location("Mensa Lothstr.", "rh", ["apa02-1rh", "apa03-1rh", "apa05-0rh", "apa06-0rh"]))

location_list.append(location.location("Mensa Pasing", "rl", ["apa15-0rl", "apa18-0rl"]))

print(jsonpickle.encode(location_list, unpicklable=False, indent=4))
