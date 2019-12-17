import csv
import json

with open("bike.json") as f:
    obj = json.load(f)
    print(obj)

with open("iris.csv") as f:
    for cols in csv.reader(f):
        print(float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3]), cols[4])
