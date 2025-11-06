"""Compare using plain dictionaries vs classes (and dataclasses).

Run this module to see the differences and common pitfalls of using dicts.
"""

from dataclasses import dataclass


def dict_style():
    # Representing users as dicts
    u1 = {"name": "Alice", "age": 30}
    u2 = {"name": "Bob", "age": "unknown"}  # wrong type

    # No encapsulation - any code can mutate fields arbitrarily
    u1["age"] = -5  # invalid but nothing stops us

    # Functions that operate on dicts need to know keys and validation
    def birthday(user):
        if not isinstance(user.get("age"), int):
            print("Cannot have birthday: age is not an int")
            return
        user["age"] += 1

    print("Dicts before:", u1, u2)
    birthday(u1)
    birthday(u2)
    print("Dicts after:", u1, u2)



class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and {self.age} years old"

    def have_birthday(self):
        if self.age < 0:
            raise ValueError("age must be non-negative")
        self.age += 1


def class_style():
    u1 = User("Alice", 30)
    u2 = User("Bob", 25)

    print("Classes before:", u1, u2)
    u1.have_birthday()
    print(u1.greet())
    print("Classes after:", u1)


if __name__ == "__main__":
    print("--- Dict style demo ---")
    dict_style()
    print("\n--- Class (dataclass) style demo ---")
    class_style()
