# Геометрическая библиотека

Реализация библиотеки для работы с простыми геометрическими фигурами (круг,прямоугольник,треугольник)

## `geometry.py`

Классы фигур

* `Circle` - круг(площадь, длина окружности, проверка точки, пересечение с другим кругом)
* `Rectangle` - прямоугольник(площадь, периметр, проверка точки, пересечение, вложенность)
* `Triangle` - треугольник(площадь по формуле, периметр, проверка валидности,проверка точки, пересечение)
* Вспомогательные функции `orientation` и `segments_intersect` для работы с отрезками

## `geometry_logic.py`

Сценарии использования

* `fill_area_with_rectangles` - заполняет область прямоугольниками одинакового размера без пересечений
* `simulate_field` - проверяет,какие фигуры полностью лежат внутри заданноо поля
* `check_placement` - ищет пересечения и вложенность между фигурами в списке

## Пример

```python
from geometry import Circle, Rectangle, Triangle
from geometry_logic import check_placement, simulate_field, fill_area_with_rectangles

circle = Circle(4, 4, 5)
rect = Rectangle(0, 0, 10, 5)
triangle = Triangle((0, 0), (4, 0), (2, 3))

print(circle.intersects(Circle(6, 6, 3)))
print(rect.contains_rectangle(Rectangle(5, 2, 3, 2)))
print(triangle.is_valid())

shapes = [circle, rect]
print(check_placement(shapes))
print(simulate_field(shapes, 50, 50))
print(fill_area_with_rectangles(20, 10, 3, 2))