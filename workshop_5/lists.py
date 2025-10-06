numbers = [99, 7, 6, 9, 10]

# for i in range(5):
#     user_input = input(f"({i}) >>> ")
#     numbers.append(int(user_input))


print(len(numbers))

print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
print("Middle element:", numbers[int(len(numbers) / 2)])
print("Middle element:", numbers[len(numbers) // 2])

print("Last element:", numbers[len(numbers) - 1])
print("Last element:", numbers[-1])
print("Previous to Last element:", numbers[-2])


odd_numbers = []
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        # print(number)
    else:
        odd_numbers.append(number)


print(f"{odd_numbers = }")
print(f"{even_numbers = }")


print(f"{numbers = }")


# numbers.remove(5)
for odd_number in odd_numbers:
    numbers.remove(odd_number)

print(f"{numbers = }")
# print(f"{5.795679456894:.2f}")
