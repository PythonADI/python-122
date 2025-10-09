"""
Create a program that will ask user for numbers indefinetely.
when user types "done" in you input you should stop taking any new numbers and do the following:

1. save each odd number in separate list
2. save each number that is divisible by 7 into separate list
3. print both list contents
"""

odd_numbers = []
numbers_divisible_by_seven = []

while True:
    user_input = input("Enter a number (type \"done\" to quit): ")
    if user_input.lower() == "done":
        print("Bye")
        break

    num = float(user_input)
    if num % 2 == 1:
        odd_numbers.append(num)
    if num % 7 == 0 :
        numbers_divisible_by_seven.append(num)


odd_numbers.sort()
numbers_divisible_by_seven.sort()
print(f"{odd_numbers = }")
print(f"{numbers_divisible_by_seven = }")

