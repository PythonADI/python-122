password_contains_upper_case = True
password_contains_lower_case = True
password_contains_number = True
password_contains_special_character = True


if password_contains_upper_case:
    if password_contains_lower_case:
        if password_contains_number:
            if password_contains_special_character:
                print("Correct password")
            else:
                print("Please include special character")
        else:
            print("Please include number")
    else:
        print("Please include lower case")
else:
    print("Please include upper case")


if not password_contains_upper_case:
    print("Please include upper case")

elif not password_contains_lower_case:
    print("Please include lower case")

elif not password_contains_number:
    print("Please include number")

elif not password_contains_special_character:
    print("Please include special character")
else:
    print("User created!")






# if password_contains_upper_case and password_contains_lower_case and password_contains_number and password_contains_special_character:
#     print("Correct password")
# else:
#     print("Password Incorrect")
