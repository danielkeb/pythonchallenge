import requests
import json
response= requests.get(url='http://api.open-notify.org/iss-now.json')

data=response.json()
#print(data)

longitud=data['iss_position'].get("longitude")
latitude=data['iss_position'].get("latitude")

#print(longitud)
is_position=(longitud, latitude)

print(is_position)

with open("data.json",'w') as f:
    json.dump(data, f )
