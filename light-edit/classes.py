class Shape:
    def __init__(self):
        self.name = 'Shape'


class Circle(Shape):
    def __init__(self):
        super().__init__()


class Triangle(Shape):
    def __init__(self):
        super().__init__()


class Parallelogram(Shape):
    def __init__(self):
        super().__init__()


class Rectangle(Parallelogram):
    def __init__(self):
        super().__init__()


class Rhombus(Parallelogram):
    def __init__(self):
        super().__init__()


def process_shapes(arg1: Shape, arg2: Triangle, arg3: Circle, arg4: Parallelogram):
    pass


parallelogram = Parallelogram()
circle = Circle()
triangle = Triangle()
rhombus = Rhombus()

process_shapes(parallelogram, triangle, circle, rhombus)
