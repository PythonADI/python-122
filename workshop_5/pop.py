import random

numbers = [2, 2, 2, 2, 2, -1, -6, 10, -7, 5, 6, ]

# print(random.randint(0, 100))


# for _ in range(100):
#     numbers.append(random.randint(-1000, 1000))


print(f"{numbers = }")

positive_numbers = []
for number in numbers.copy():
    if number > 0:
        positive_numbers.append(number)
        numbers.remove(number)

print(f"{positive_numbers = }")