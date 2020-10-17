import json, random, requests
import country_converter as coco

OWM_API_KEY = "1f4ebc962bb46caeb74ac2f5ec662fd4"

filepath = './city.list.json'
with open(filepath, encoding="utf-8") as f:
    data = json.load(f)


def getRandCity():
    index = random.randint(0, len(data) - 1)
    city_data = data[index]
    city_info = {
        "id": city_data["id"],
        "name": city_data["name"],
        "country": coco.convert(names=city_data["country"], to="name_short")
    }
    return city_info


def getWeatherById(id):
    api_call = f"http://api.openweathermap.org/data/2.5/weather?id={id}&appid={OWM_API_KEY}"
    response_json = requests.get(api_call).json()
    return response_json['weather'][0]


def generateRandomWeatherTweet():
    rand_city = getRandCity()
    weather = getWeatherById(rand_city['id'])

    while(weather['main'] != 'Rain'):
        rand_city = getRandCity()
        weather = getWeatherById(rand_city['id'])

    string_formats = [
        f"{rand_city['name']}, {rand_city['country']} is currently experiencing {weather['description']}",
        f"there is {weather['description']} in {rand_city['name']}, {rand_city['country']} today",
        f"{weather['description']} today in {rand_city['name']}, {rand_city['country']}",
        f"{rand_city['name']}, {rand_city['country']} is currently experiencing {weather['description']}"
    ]
    index = random.randint(0, len(string_formats) - 1)
    return string_formats[index]

#print(string)
