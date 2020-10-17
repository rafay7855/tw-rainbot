import tweepy
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
    tweet_string = string_formats[index]
    # If string is too long, generate another.
    if len(tweet_string) > 240:
        tweet_string = generateRandomWeatherTweet()
        return tweet_string


# Authenticate to Twitter
auth = tweepy.OAuthHandler("EmCWw02kB6OzvsapIiQ7DhaRC", "2tEtWpx0i5JPmv9rtN4PE13udiDuSfQar6Qapkv3rQgNi7ddc7")
auth.set_access_token("4109292376-6IbVa6CslXtpSdwDjqj0XGVgxfL94xZwl5mdFZY", "KWWhmWUyDqJNtEj1kfE8XmZKG53dsVXSqwNBeiMVdMtLS")

api = tweepy.API(auth)

if api.verify_credentials():
    print("Authentication OK")
else:
    print("Error during authentication")
