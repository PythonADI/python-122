grade = 5

if grade >= 90:
    print("A - Excellent!")
elif grade >= 80:
    print("B - Good job!")
elif grade >= 70:
    print("C - Not bad.")
elif grade >= 60:
    print("D - You need to study more.")
else:
    print("F - You failed.")



# using and


if 90 <= grade and grade <= 100:
    print("A")   
elif 80 <= grade and grade < 90:
    print("B") 
elif grade < 80 and grade >= 70:
    print("C")
elif 60 <= grade < 70:
    print("D")

