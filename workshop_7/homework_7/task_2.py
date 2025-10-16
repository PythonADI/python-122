
import random
"""
def think_of_a_number():
    return random.randint(0, 100)


x = think_of_a_number()
y = think_of_a_number()

is_x_higher_user_prediction = input("Is x higher than y? ").lower() == "yes"
is_x_higher = x > y

if is_x_higher and is_x_higher_user_prediction:
    print("KUDOS you guessed it!")
else:
    print("Try again")

print(x)
print(y)
"""

# ------
names = ["Nick", "Nino", "Luka", "George", "David", "Marry"]

# print(names[random.randint(0, len(names) - 1)])
print(random.choice(names))

def random_user():
    return {
        "name": random.choice(names),
        "age": random.randint(13, 100),
        "has_pet": random.randint(0, 100) <= 20,
        # "has_pet": random.choice((True, False))
    }

def generate_random_users(user_count):
    users = []

    for _ in range(user_count):
        users.append(random_user())
    
    return users


def multiple_value_return():
    return 5, 8

users = []


users.extend(generate_random_users(10))

print(len(users))
users.extend(generate_random_users(100))


print(len(users))


print(multiple_value_return())
print(type(multiple_value_return()))

a, b = (7, 8)
x, y = multiple_value_return()
