import random
numbers = []

for _ in range(10):
    numbers.append(random.randint(-100, 100))

sorted_before_index = 0

for _ in numbers:
    min_value = numbers[sorted_before_index] # დავუშვათ, რომ ეს რიცხვი არის უმცირესი დაულაგებელი ნაწილიდან
    min_value_index = sorted_before_index

    # unsorted_part = numbers[sorted_before_index + 1:]
    # for i, num in enumerate(unsorted_part, start=sorted_before_index + 1):
    #     if num < min_value:
    #         min_value = num
    #         min_value_index = i

    numbers.pop(min_value_index)
    numbers.insert(sorted_before_index, min_value)
    sorted_before_index += 1


print(numbers)
