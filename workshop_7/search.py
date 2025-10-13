import random
numbers = []

for _ in range(10):
    numbers.append(random.randint(-100, 100))

# numbers = [-500, -150, -100, -50, 10, 15, 5, 50, 100, 150]
numbers.sort() # You cannot use binary serach on unsorted list!!!!

print(numbers)
# Linear Search / Brute Force
# for i, num in enumerate(numbers):
#     if num == -50:
#         print(f"Found it at: {i}")
#         break



# binary Search
search_number = -50
low = 0
high = len(numbers) - 1

while low <= high:
    mid = low + (high - low) // 2

    if numbers[mid] == search_number:
        print(f"Found it at: {mid}")
        break

    if numbers[mid] < search_number:
        low = mid + 1
    else:
        high = mid - 1
        

