def greet(user, age):
    print(f"Hi {user}, you are {age} years old!")


def is_adult_check(student):
    age = student["age"]
    user = student["name"]

    if age >= 18:
        print(f"{user} is adult")
    elif age >= 13:
        print(f"{user} is teenager")
    else:
        print(f"{user} is minor")



def upper_and_reverse(name):
    return name[::-1].upper()

# Use case of greet
students = [
    {
        "name": "Nick",
        "age": 25
    },
    {
        "name": "George",
        "age": 12
    },
    {
        "name": "Nelson",
        "age": 17
    }
]

for student in students:
    greet(student["name"], student["age"])
    is_adult_check(student)
    print(upper_and_reverse(student["name"]))
