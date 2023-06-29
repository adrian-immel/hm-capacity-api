import requests
import location
import time


def get_location_data(loc: location):
    url = "http://graphite-kom.srv.lrz.de/render/?from=-1hours&target=ap.ap*-?" + loc.lrz_subdistrict_id + "*.ssid.*&format=json"
    time.sleep(1)
    data_list = requests.get(url, timeout=30).json()
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


