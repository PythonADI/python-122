"""Shape examples: base class and derived shapes showing simple polymorphism"""

class Shape:
    def area(self):
        raise NotImplementedError("area() must be implemented by subclasses")


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        import math

        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Circle(2)]
    for s in shapes:
        print(f"{s.__class__.__name__} area: {s.area():.2f}")
