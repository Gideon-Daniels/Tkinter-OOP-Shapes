class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side
        print("I am a : " + self.name)

    def Area(self):
        return "I am a " + self.name + "\n" + "I have so many " + self.side


obj_shape = Shapes("shape", "sides")
print(obj_shape.Area())


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def Area(self):
        results = self.length * self.width
        return results


obj_book = Rectangle(10, 7)
obj_screen = Rectangle(5, 7)
print("The area of a book is: ", obj_book.Area())
print("The area of a screen is: ", obj_screen.Area())

# Circle


class Circle(Shapes):
    def __init__(self, rad):
        self.radius = rad

    def Area(self):
        results = int(3.14 * self.radius * self.radius)
        return results


obj_coin = Circle(5)
print("The area of this coin is : ", obj_coin.Area())

# Triangle


class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def Area(self):
        results = 0.5 * self.base * self.height
        return results


obj_tri = Triangle(5, 8)
print("The area of a triangle is:", obj_tri.Area())
