import random


def generate_random_numbers(n, start=0, end=10):
    nums = [] # shadows nums variable from outside (global scope)
    for _ in range(n):
        nums.append(random.randint(start, end))
    return nums

nums = generate_random_numbers(n=10, start=5, end=10)

nums2 = generate_random_numbers(12)

nums3 = generate_random_numbers(200, 0, 100)

nums.extend(generate_random_numbers(10, -10, 0))

print(nums)
print(nums2)
print(nums3)

