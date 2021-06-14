import requests
import json
import time

choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")

if choice == "y":
    print('OK, we \'ll go with the hard-coded token.')
    accessToken = "Bearer Mjk3NWE2YTMtZGMxNy00ZTZjLTk0ZWItMDRkYzY2MzJlMDkzODliODYwMTktY2Q4_PF84_consumer"

elif choice == "n":
    print('This wil not have the desired outcome.')
    quit()  

else:
	accessToken = "Bearer Mjk3NWE2YTMtZGMxNy00ZTZjLTk0ZWItMDRkYzY2MzJlMDkzODliODYwMTktY2Q4_PF84_consumer"

print(accessToken)

r = requests.get(   "https://webexapis.com/v1/rooms",
                    headers = {"Authorization": accessToken}
                )

print("List of rooms:")
print(r)
rooms = r.json()["items"]
for room in rooms:
    print(room['title'] + room['type'])