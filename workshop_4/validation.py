
while True:
    while True:
        user_input = input("Enter number: ")

        if user_input.isdigit():
            number = int(user_input)
            break
        else:
            print("Please enter correct number, my program cannot work with letters")

    while True:
        user_input = input("Enter number 2: ")

        if user_input.isdigit():
            number2 = int(user_input)
            break
        else:
            print("Please enter correct number, my program cannot work with letters")

    print(type(number), number)
    print(type(number2), number2)
    print(number + number2)



# while True:
#     expression = input("Expression: ")
#     print(eval(expression))



# print(type(user_input), user_input)
# print(type(number), number)
# print(number + 1)

































print(len(user_input))

ascii_numbers = "0123456789"
is_correct_number = True

for c in user_input:
    if c not in ascii_numbers:
        print("Incorrect Number!")
        is_correct_number = False
        break
    
if is_correct_number:
    number = int(user_input)
    print(f"Converted to int: {number}")
else:
    print("Please input correct number, could not convert to int!")
