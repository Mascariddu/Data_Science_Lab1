import json
from math import cos, acos, sin

# es 1
with open("bike.json") as f:
    obj = json.load(f)

# es 2
activeStations = [station for station in obj["network"]["stations"] if station["extra"]["status"] == "online"]

print("Number of active stations:", len(activeStations))

# es 3
freeBikes = sum([station["free_bikes"] for station in obj["network"]["stations"]])
freeDocks = sum([ station["empty_slots"] for station in obj["network"]["stations"]])

print("Available bikes:", freeBikes)
print("Available docks:", freeDocks)

# es 4


def distance_coords(lat1, lng1, lat2, lng2):
    deg2rad = lambda val: val * 3.141592 / 180
    lat1, lng1, lat2, lng2 = map(deg2rad, [lat1, lng1, lat2, lng2])
    r = 6378100  # Radius of the Earth, in meters
    return r * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))


lat = 45.034512
lng = 7.644419
minDist = 1000000000
name = None

for x in obj["network"]["stations"]:
    if x["free_bikes"] > 0:
        if distance_coords(lat, lng, x["latitude"], x["longitude"]) < minDist:
            name = x["name"]
            minDist = distance_coords(lat, lng, x["latitude"], x["longitude"])

print("The closest station is", name, "that is distant", round(minDist, 2), "meters")
