import json 

import requests 

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=12345,us&appid=20cf75f89cf07e87478e3f145b9120a8') 

data=r.json() 

print(data) 