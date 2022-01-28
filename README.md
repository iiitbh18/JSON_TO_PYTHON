# JSON_TO_PYTHON
This we can see some examples of how to convert json data to python. <br>
first import json. <br>
make a json data. <br>
load that json data in  to  python by using json.loads(json_data). <br>





To make an api call:- <br>
import requests. <br>
a = requests.get('url')   like ----- a = requests.get('https://api.openaq.org/v1/measurements?city=Amsterdam') <br>
print(a.status_code)  if 200 come then our is successful . <br>
we can print the data of that Api call using the method a.json() . <br>
print(a.url)  ### we can get the url also . <br>
we can also filter our result. <br>








