number = None
number2 = None

def is_valid_number(user_input):
    valid_symbols = "0123456789"

    num = user_input
    if user_input[0] in "+-":
        num = user_input[1:]
    dot_found = False
    for ch in num:
        if ch == "." and dot_found:
            return False
        elif ch == "." and not dot_found:
            dot_found = True
            continue

        if ch not in valid_symbols:
            return False
    
    return True


def input_number():
    while True:
        user_input = input("Enter number: ")
        if is_valid_number(user_input):
            number = float(user_input)
            if user_input[0] == "-":
                number *= -1
            return number
        else:
            print("Please enter valid number!")


number = input_number()
number2 = input_number()

print(number)

print(number2)
print(number + number2)