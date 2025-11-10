"""Person inheritance examples: Person, Employee, Student"""

class Person:
    def __init__(self, name: str):
        self.name = name

    def info(self) -> str:
        return f"Person: {self.name}"

    def __str__(self):
        return self.info()

class Employee(Person):
    def __init__(self, name: str, role: str):
        super().__init__(name)
        self.role = role

    def info(self) -> str:
        return f"Employee: {self.name}, role: {self.role}"


class Student(Person):
    def __init__(self, name: str, school: str):
        super().__init__(name)
        self.school = school

    def info(self) -> str:
        return f"Student: {self.name}, school: {self.school}"



if __name__ == "__main__":
    people = [Person("Alex"), Employee("Beth", "Engineer"), Student("Carl", "High School")]
    for p in people:
        print(p)