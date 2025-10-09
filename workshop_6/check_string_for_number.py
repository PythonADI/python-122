unique_string = input(">>> ")
valid_symbols = "0123456789"
# if unique_string.startswith('-') or unique_string.startswith("+"):
num = unique_string
if unique_string[0] in "+-":
    num = unique_string[1:]


number_is_valid = True
dot_found = False
for ch in num:
    if ch == "." and dot_found:
        print("Please enter valid number")
        number_is_valid = False
        break
    elif ch == "." and not dot_found:
        dot_found = True
        continue

    if ch not in valid_symbols:
        print("Please enter valid number")
        number_is_valid = False
        break

        

    # for valid_symbol in valid_symbols:
    #     is_valid = False
    #     if valid_symbol == ch:
    #         is_valid = True
    #         break
            

    # if not is_valid:
    #     print("Please enter correct number!")
    #     break

    # print(ch)

if number_is_valid:
    num = float(unique_string)
    print(num)
