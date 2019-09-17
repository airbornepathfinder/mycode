#!/usr/bin/env python3

import requests

LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=27606&date=2019-09-19&distance=25&API_KEY=40464261-88A9-4651-8C92-ADB870E1770D'

def main():

    r = requests.get(LOOKUPAPI)

    print("Weather Forecast")
    print("----------------")

    for x in r.json():
        print(x.get("DateForecast"))
        print("---------")
        print(x.get("Discussion"))

main()

