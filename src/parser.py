import requests
import location


def get_location_data(loc: location):
    url = "http://graphite-kom.srv.lrz.de/render/?from=-1hours&target=ap.ap*-?" + loc.lrz_subdistrict_id + "*.ssid.*&format=json"
    data_list = requests.get(url, timeout=30).json()
    if not data_list or None:
        raise ConnectionError("Could not get or parse the json from LRZ")
    if loc.specific_access_points is not None:
        for ap in data_list:
            for i in loc.specific_access_points:
                if i in ap["target"]:
                    datapoint = ap["datapoints"][-2]
                    loc.timestamp = datapoint[1]
                    loc.update_clients(datapoint[0])
    else:
        for ap in data_list:
            datapoint = ap["datapoints"][0]
            loc.timestamp = datapoint[1]
            loc.update_clients(datapoint[0])


def percentage_calculator(loc: location):
    percent = loc.clients / loc.static_max_clients
    percent = round(percent, 2)
    if percent > 1:
        percent = 1.0
    return percent
