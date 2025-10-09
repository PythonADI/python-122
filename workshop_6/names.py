students = []

while True:
    username = input("Username: ")
    if username.lower() == "done":
        break
    score = int(input("Score: "))

    students.append([username, score])


# print(students[0])
# print(students[0][0])
# print(students[0][1])

# for student in students:
#     print(f"{student[0]} has {student[1]} grade")

for name, score in students:
    print(f"{name} has {score} grade")
