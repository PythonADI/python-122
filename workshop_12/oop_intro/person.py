"""Simple Person class showing attributes and methods"""

class Person:
    def __init__(self, name, age):
        # initialzer / constructor
        # attributes / fields
        self.name = name
        if age < 0 or 150 < age:
            raise ValueError("age should be in reasonable range (0, 150)")
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sit(self):
        print(f"{self.name} sat down")
    
    def roll(self):
        print(f"{self.name} rolled over")

    def have_birthday(self):
        self.age += 1



student = Person("George", 17)
lecturer = Person("Nick", 30)
doggo = Dog("Jeka", 7, "Doberman")

student.have_birthday()
print(student.greet())
lecturer.have_birthday()
print(lecturer.greet())

print(doggo.name, doggo.age, doggo.breed)
doggo.have_birthday()
print(doggo.name, doggo.age, doggo.breed)
doggo.roll()

people = [
    Person("Lyla", 19),
    Person("Nicky", 22)
]




for person in people:
    print(person.greet())

# student = {
#     "name": "George",
#     "age": 17
# }

# lecturer = {
#     "name": "Nick",
#     "age": 30,
#     "pet": "Dog"
# }

# print(student["name"], student["age"], student["pet"])
# print(lecturer["age"], lecturer["name"], lecturer["pet"])




