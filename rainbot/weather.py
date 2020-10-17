import json, random

filepath = './city.list.json'

with open(filepath, encoding="utf-8") as f:
    data = json.load(f)

print(len(data))

index = random.randint(0, len(data) - 1)
print(index)
print(data[index])

city_info = data[index]
city_name = city_info['name']
city_country = city_info['country']
city_id = city_info['id']

string = f"It is raining in {city_name}, {city_country}."
print(string)