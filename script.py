import requests

#r = requests.post("127.0.0.1:5000/weather")
r =requests.post("127.0.0.1:5000/weather", data={"course":"Cs173"})
print(r.get_json())
