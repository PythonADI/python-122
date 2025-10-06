numbers = [1, 2, 3, 4, 5, 6, 11]

# for i in range(2):
#     print(numbers[i])


# for num in numbers[0:2]:
#     print(num)

for num in numbers[:2]:
    print(num)

print("-" * 10)

for num in numbers[2:4]:
    print(num)

print("EVENS indicies")
for num in numbers[::2]:
    print(num)


print("ODDS indicies")
for num in numbers[1::2]:
    print(num)



print("index divisible by 3")
for num in numbers[::3]:
    print(num)