while True:
    user_input = input(">>> (press enter to continue) ")

    if user_input == "quit" or user_input == "exit":
        print("Thank you")
        break

    
    user_input = input(">>> ")

    if not user_input.isdigit():
        print("Please enter correct number")
        continue
    
    num1 = int(user_input)

    user_input = input(">>> ")

    if not user_input.isdigit():
        print("Please enter correct number")
        continue
    
    num2 = int(user_input)

    print(f">>> {num1 + num2}")
