#!/bin/python3

import requests
import json
import sys

def locate():
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,country,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,reverse,mobile,proxy")
    resp = data.json()
    print("\nAdresse ip tracker avec succées !\n")
    print("Status: " + resp["status"])
    if resp["status"] == "erreur d'adresse ip":
        print("E-Message: " + resp["message"])
        sys.exit()
    print("Continent : " + resp["continent"])
    print("Country : " + resp["country"])
    print("Region: " + resp["region"])
    print("Region Name : " + resp["regionName"])
    print("City : " + resp["city"])
    print("District : " + resp["district"])
    print("Zip : " + resp["zip"])
    print("Latitude : " + str(resp["lat"]))
    print("Longitude : " + str(resp["lon"]))
    print("Timezone : " + resp["timezone"])
    print("Currency : " + resp["currency"])
    print("ISP : " + resp["isp"])
    print("ORG : " + resp["org"])
    print("AS : " + resp["as"])
    print("AS Name : " + resp["asname"])
    print("Reverse : " + resp["reverse"])
    print("Mobile : " + str(resp["mobile"]))
    print("Proxy : " + str(resp["proxy"]))

print("IP TRACKING TOOL")
print("Twitter : @MaitreTrunk  | Github : MaitreTrunk ")


ip = input("Indique l'adresse IP exemple: 0.0.0.0 ou l'url du site exemple: site.fr \nAdresse/Url = ")
locate()
