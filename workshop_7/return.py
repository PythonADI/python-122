def input_number():
    # local scope
    number = int(input("Enter Number: ")) # shadows the number variable in global scope
    return number


number = input_number()
number2 = input_number()
print(number + number2)
