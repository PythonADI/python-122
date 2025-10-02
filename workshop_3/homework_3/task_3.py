
# if 5 % 2 == 0:
#     is_even = True
# else:
#     is_even = False
number = int(input("think of a number: "))
# is_even = True if number % 2 == 0 else False

is_even = number % 2 == 0
text = "Is even" if is_even else "Is Odd"

print(f"{number} {text}")


