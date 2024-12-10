import math


class Figure:
    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = color
        self.sides_count = len(sides) if len(sides) == self.sides_count else self.sides_count
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count


    def filled(self):
        return True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all([isinstance(x, int) for x in (r, g, b)]) and all([0 <= x <= 255 for x in (r, g, b)])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, new_sides):
        return (
            isinstance(new_sides, tuple)
            and len(new_sides) == self.sides_count
            and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


### Класс `Circle`
class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *side):
        super().__init__(color, side)
        self.__radius = side[0] / (2 * 3.14)

    def radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * self.radius ** 2


### Класс `Triangle`
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), a=1, b=1, c=1):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


### Класс `Cube`
class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), edge_length=1):
        super().__init__(color, *(edge_length,) * self.sides_count)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3




if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    print(circle1.radius())

    # Проверка объёма (куба):
    print(cube1.get_volume())






