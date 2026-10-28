import math


class Circle:
    """Класс, представляющий круг

    Args:
        center_x (float): Координата x центра круга
        center_y (float): Координата y центра круга
        radius (float): Радиус круга
    
    """
    def __init__(self, center_x, center_y, radius):
        
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        """Вычисляет площадь круга

        Returns:
            float: Площадь
        """
        return math.pi * self.radius**2

    def circumference(self):
        """Вычисляет длину окружности

        Returns:
            float: длина  окружности
        """
        return 2 * math.pi * self.radius

    def contains_point(self, x, y):
        """Проверяет,лежит ли точка внутри круга

        Args:
            x (float): Координата x точки
            y (float): Координата y точки
        Returns:
            bool: True, если точка внутри круга или на его границе, иначе False 
        """
        return (self.center_x - x) ** 2 + (self.center_y - y) ** 2 <= self.radius**2

    def intersects(self, other):
        """Проверяет, пересекаются ли круги

        Args:
            other (Circle): Другой круг
        Returns:
            bool: True, если пересекаются, иначе False 
        """
        return (self.center_x - other.center_x) ** 2 + (
            self.center_y - other.center_y
        ) ** 2 <= (self.radius + other.radius) ** 2


class Rectangle:
    """Класс, представляющий прямоугольник

    Args:
        x (float): Координата x левой верхней вершины прямоугольника
        y (float): Координата y левой верхней вершины прямоугольника
        width (float): Ширина прямоугольника
        height (float): Длина прямоугольника
    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        """Вычисляет площадь прямоугольника

        Returns:
            float: Площадь
        """
        return self.width * self.height

    def perimeter(self):
        """Вычисляет периметр прямоугольника

        Returns:
            float: Периметр
        """
        return (self.width + self.height) * 2

    def contains_point(self, x, y):
        """Проверяет,лежит ли точка внутри прямоугольника

        Args:
            x (float): Координата x точки
            y (float): Координата y точки
        Returns:
            bool: True, если точка внутри или на прямоугольнике, иначе False 
        """
        a, b, c, d = self.x, self.y, self.width, self.height
        return (x <= a + c) and (y <= b + d) and (x >= a) and (y >= b)

    def intersects(self, other):
        """Проверяет,пересекаются ли прямоугольники

        Args:
            other (Rectangle): Другой прямоугольник
        Returns:
            bool: True, если прямоугольники пересекаются, иначе False 
        """
        a, b, c, d = self.x, self.y, self.width, self.height
        a2, b2, c2, d2 = other.x, other.y, other.width, other.height
        return not ((a + c <= a2) or (a >= a2 + c2) or (b >= b2 + d2) or (b + d <= b2))

    def contains_rectangle(self, other):
        """Проверяет, вложен ли один прямоугольник в другой

        Args:
            other (Rectangle): Другой прямоугольник
        Returns:
            bool: True, если один вложен в другой, иначе False 
        """
        a, b, c, d = self.x, self.y, self.width, self.height
        a2, b2, c2, d2 = other.x, other.y, other.width, other.height
        return (a <= a2) and (a + c >= a2 + c2) and (b <= b2) and (b + d >= b2 + d2)


class Triangle:
    """Класс, представляющий треугольник

    Args:
        a (tuple): Координаты вершины a
        b (tuple): Координаты вершины b
        c (tuple): Координаты вершины c
    
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        ax, ay = a
        bx, by = b
        cx, cy = c

        self.ab = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        self.bc = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
        self.ca = math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)

    def perimeter(self):
        """Вычисляет периметр треугольника

        Returns:
            float: Периметр
        """
        return self.ab + self.bc + self.ca

    def area(self):
        """Вычисляет площадь треугольника

        Returns:
            float: Площадь
        """
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))

    def is_valid(self):
        """Проверяет возможность создания треугольника

        Returns:
            bool: True, сумма длин каких-либо двух сторон больше третьей, иначе False  
        """
        return (
            (self.ab < self.bc + self.ca)
            and (self.bc < self.ab + self.ca)
            and (self.ca < self.bc + self.ab)
        )

    def contains_point(self, f):
        """Проверяет,лежит ли точка внутри треугольника

        Args:
            f (tuple): Координаты точки f
        Returns:
            bool: True, если точка внутри или на треугольнике, иначе False 
        """
        s = self.area()
        s1 = Triangle(self.a, self.b, f).area()
        s2 = Triangle(self.b, self.c, f).area()
        s3 = Triangle(self.c, self.a, f).area()

        return abs(s - (s1 + s2 + s3)) < 1e-9


    def intersects(self, other):
        """Проверяет, пересекаются ли треугольники

        Args:
            other (Triangle): Другой треугольник
        Returns:
            bool: True, если пересекаются, иначе False 
        """
        sides1 = [(self.a, self.b), (self.b, self.c), (self.c, self.a)]
        sides2 = [(other.a, other.b), (other.b, other.c), (other.c, other.a)]

        for a, b in sides1:
            for c, d in sides2:
                if segments_intersect(a, b, c, d):
                    return True

        for point in (other.a, other.b, other.c):
            if self.contains_point(point):
                return True
        for point in (self.a, self.b, self.c):
            if other.contains_point(point):
                return True

        return False

def orientation(p, q, r):
        """Вспомогательная функция, узнает где расположена точка относительно отрезка
        
        Args:
            p (tuple): Координаты вершины p
            q (tuple): Координаты вершины q
            r (tuple): Координаты вершины r
        Returns:
            Literal :-1,если точка справа по направлению относительно отрезка.
            0,если точка на  отрезке.
            1,если точка расположена слева по направлению относительно отрезка
        """
        val = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else -1

def segments_intersect(p1, q1, p2, q2):
        """Вспомогательная функция, узнает пересекаются ли отрезки
        
        Args:
            p1 (tuple): Координаты точки p1
            q1 (tuple): Координаты вершины q1
            p2 (tuple): Координаты вершины p2
            q2 (tuple): Координаты вершины q2
        Returns:
            bool: True, если пересекаются, иначе False
        """
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True

        return False


