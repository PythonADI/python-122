import traceback
while True:
    try:
        a = float(input("Text: "))
        b = float(input("Text: "))
        print(a / b)
        # print(str(a) / b)
        break
    except ValueError:
        print("Please enter correct number!")
    except ZeroDivisionError:
        print("Divisor must be non zero value")
    except Exception as e:
        print("Unexpected error!")
        print(e)
        with open("./test.log", "a") as f:
            f.write(traceback.format_exc())
    finally:
        print("I'll be executed anyway")
