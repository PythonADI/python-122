person = {
    "name": "Luka",
    "age": 27,
    "pet": "Dog",
    "friends": ["Nick", "Marry"]
}

print(person)
print(person["name"])

person["name"] = "Gio"
print(person)
person.pop("pet")
print(person)

person["city"] = "New York"
print(person)



for key in person.keys():
    print(key)


for value in person.values():
    print(value)


# for item in person.items():
#     print(item[0], item[1])
for key, value in person.items():
    print(f"{key}: {value}")