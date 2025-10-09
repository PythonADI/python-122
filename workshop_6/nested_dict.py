students = []

while True:
    username = input("Username: ")
    if username.lower() == "done":
        break
    score = int(input("Score: "))

    students.append({
        "name": username,
        "score": score
    })


s = 0

for student in students:
    print(student["name"], student["score"])
    s += student["score"]

print(type(students[0]))
print(f"Total Score: {s}")
print(f"Average Score: {s / len(students)}")

