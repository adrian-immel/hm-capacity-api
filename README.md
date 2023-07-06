# hm-capacity-api
This is an API that provides the current capacity of the canteen and library for the University of applied silences munich. It gets its data from the current Clients connected to the Wi-Fi of the canteen and library. For that it uses a Public API provided by the LRZ.

## Usage
### Host on GitHub Pages
The API can be hosted on GitHub Pages and is updated via the GitHub Actions script:"static.yml" , this is not recommended because the GitHub Actions script needs to be run very often to provide up-to-date data.

### Host on your own server
You can host the API on your own server. Just use the provided docker image to tun it on your server.
The docker updates the data every 5 minutes, but do to a bug at LRZ we have to use a data-pint that is 5 minutes old or else the provided data would not be very accurate.
Be careful the docker does not provide a webserver. You have to use a webserver like nginx to provide the API via HTTP.
You can use the example docker-compose.yml to run the API Container on your server. \
In the container the files are located at /hm-dates-api/.

## API
The API provides you with the data in a JSON format.
The data is available for the following locations:
+ Bibliothek_H_Bau
+ Bibliothek_I_Bau
+ Bibliothek_L_Bau
+ Cafeteria_Karlstr
+ Mensa_Lothstr
+ Mensa Pasing

To get the data for a location you have to send a GET request to the API with the path hm-capacity-api/LOCATION.json.
Alternatively you can send a GET request to the API with the path hm-capacity-api/all.json to get the data for all locations.

Example for a GET request to get the data for all locations:
```http
GET https://YOURDOMAIN/hm-capacity-api/Mensa_Lothstr.json
```

The Attributes of the JSON are:
For example for the location "Mensa_Lothstr":

```json
{
    "name": "Mensa_Lothstr.",
    "lrz_subdistrict_id": "rh",
    "static_max_clients": 280,
    "specific_access_points": [
        "apa02-1rh",
        "apa03-1rh",
        "apa05-0rh",
        "apa06-0rh"
    ],
    "clients": 97,
    "capacity_level_in_percent": 0.35,
    "timestamp": 1688556300
}
```
Attributes:
1. name (string): The name or identifier of the cafeteria. In this case, it is "Mensa_Lothstr."

2. lrz_subdistrict_id (string): An identifier for the LRZ subdistrict associated with the location. In this case, the identifier is "rh."

3. static_max_clients (integer): The maximum number of clients or customers the cafeteria can accommodate. The value provided is 280.

4. specific_access_points (array): An array of specific access point identifiers within the location. Each identifier represents a unique access point.

5. clients (integer): The current number of clients or customers present in the cafeteria. The value provided is 97.

6. capacity_level_in_percent (float): The current capacity level of the cafeteria, expressed as a percentage. The value provided is 0.35, which corresponds to 35% capacity.

7. timestamp (integer): A timestamp indicating when the data was recorded. The value provided is 1688556300, representing a specific point in time (Unix timestamp).