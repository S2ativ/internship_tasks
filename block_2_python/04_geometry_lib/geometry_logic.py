from geometry import Triangle, Rectangle, Circle, segments_intersect

def fill_area_with_rectangles(area_width, area_height, rect_width, rect_height):
    """Функция размещает прямоугольники заданного размера внутри области без пересечений.
    Прямоугольники размещаются последовательно, начиная с левого верхнего угла области(0, 0).

    Args:
        area_width (float): Ширина области
        area_height (float): Высота области
        rect_width (float): Ширина размещаемых прямоугольников
        rect_height (float): Высота размещаемых прямоугольников
    
    Returns:
        dict: Словарь с результатами размещения, содержащий следующие ключи:
            placed_count (int): Количество успешно размещенных прямоугольников
            rectangles (list): Список координат размещенных прямоугольников.Каждый элемент списка — это словарь с ключами:
                x (int): Координата X верхнего левого угла прямоугольника
                y (int): Координата Y верхнего левого угла прямоугольника
    """
    rectangles = []

    y = 0
    while y + rect_height <= area_height:
        x = 0
        while x + rect_width <= area_width:
            rectangles.append({'x': x, 'y': y})
            x += rect_width
        y += rect_height

    return {
        'placed_count': len(rectangles),
        'rectangles': rectangles
    }


def simulate_field(shapes, area_width, area_height):
    """Функция проверяет, все ли фигуры из списка находятся внутри заданного прямоугольного поля
    
    Args:
        shapes (list): Список объектов геометрических фигур (Circle, Rectangle, Triangle)
        area_width (int): Ширина поля
        area_height (int): Высота поля
    
    Returns:
        dict: Словарь с результатами проверки:
            inside_count (int): Количество фигур, полностью находящихся внутри поля
            outside_figures (list[dict]): Список фигур, которые выходят за границы поля.Каждый элемент списка — это словарь с ключами:
                figure: Объект фигуры
                reason (str): Причина выхода за границы
    """
    inside_count = 0
    outside_figures = []

    for figure in shapes:
        inside = True
        reason = None

        if isinstance(figure, Rectangle):
            if (figure.width + figure.x > area_width) or (figure.height + figure.y > area_height) or (figure.x < 0) or (figure.y < 0):
                inside = False
                reason = 'Выходит за границы поля'

        elif isinstance(figure, Circle):
            if (figure.center_x + figure.radius > area_width) or (figure.center_x - figure.radius < 0) or (figure.center_y + figure.radius > area_height) or (figure.center_y - figure.radius < 0):
                inside = False
                reason = 'Выходит за границы поля'

        elif isinstance(figure, Triangle):
            points = [figure.a, figure.b, figure.c]
            for point in points:
                x, y = point
                if x < 0 or x > area_width or y < 0 or y > area_height:
                    inside = False
                    reason = 'Выходит за границы поля'
                    break
        
        if inside:
            inside_count +=1
        else:
            outside_figures.append({
                'figure': figure,
                'reason': reason
            })
    
    return {
        'inside_count': inside_count,
        'outside_figures': outside_figures
    }

def check_placement(shapes):
    """Функция анализирует взаимное расположение фигур из списка
    
    Args:
        shapes (list): Список объектов геометрических фигур (Circle, Rectangle, Triangle)
    
    Returns:
        list (dict): Список словарей, где каждый словарь содержит:
            type (str): "intersection" или "containment"
            figures (list): Список фигур, участвующих во взаимодействии 
    """
    result = []
    n = len(shapes)

    for i in range(n):
        for j in range(i+1, n):
            fig1 = shapes[i]
            fig2 = shapes[j]

            intersects = False

            if type(fig1) == type(fig2):
                intersects = fig1.intersects(fig2)
            else:
                if isinstance(fig1, Rectangle) and isinstance(fig2, Circle):
                    intersects = rect_circle_intersects(fig1, fig2)
                elif isinstance(fig2, Rectangle) and isinstance(fig1, Circle):
                    intersects = rect_circle_intersects(fig2, fig1)

                elif isinstance(fig1, Rectangle) and isinstance(fig2, Triangle):
                    intersects = rect_triangle_intersects(fig1, fig2)
                elif isinstance(fig2, Rectangle) and isinstance(fig1, Triangle):
                    intersects = rect_triangle_intersects(fig2, fig1)

                elif isinstance(fig1, Circle) and isinstance(fig2, Triangle):
                    intersects = circle_triangle_intersects(fig1, fig2)
                elif isinstance(fig2, Circle) and isinstance(fig1, Triangle):
                    intersects = circle_triangle_intersects(fig2, fig1)

            if intersects:
                result.append({
                    'type': 'intersection',
                    'figures': [fig1, fig2]
                })
                continue

            if  contains(fig1, fig2):
                result.append({
                    'type': 'containment',
                    'figures': [fig1, fig2]
                })
            elif contains(fig2, fig1):
                result.append({
                    'type': 'containment',
                    'figures': [fig2, fig1]
                })

    return result


def rect_circle_intersects(rect, circle):
    """Вспомогательная функция, проверяет,пересекаются ли прямоугольник и круг
       
         Args:
            rect (Rectangle): прямоугольник
            circle (Circle): круг
        Returns:
            bool :True, если квадрат расстояния от центра круга до ближайшей точки прямоугольника <= квадрата радиуса, иначе False 
    """
    close_x = max(rect.x, min(circle.center_x, rect.x + rect.width))
    close_y = max(rect.y, min(circle.center_y, rect.y + rect.height))

    dx = circle.center_x - close_x
    dy = circle.center_y - close_y
    return dx*dx + dy*dy <= circle.radius * circle.radius

def rect_triangle_intersects(rect, triangle):
    """Вспомогательная функция, проверяет,пересекаются ли прямоугольник и треугольник
        
        Args:
            rect (Rectangle): прямоугольник
            triangle (Triangle): треугольник
        Returns:
            bool :True, прямоугольник и треугольник пересекаются, иначе False 
    """
    rect_sides = [
        ((rect.x, rect.y), (rect.x + rect.width, rect.y)),
        ((rect.x + rect.width, rect.y), (rect.x + rect.width, rect.y + rect.height)),
        ((rect.x + rect.width, rect.y + rect.height), (rect.x, rect.y + rect.height)),
        ((rect.x, rect.y + rect.height), (rect.x, rect.y))
    ]
    tri_sides = [
        (triangle.a, triangle.b),
        (triangle.b, triangle.c),
        (triangle.c, triangle.a)
    ]

    for r1, r2 in rect_sides:
        for t1, t2 in tri_sides:
            if segments_intersect(r1, r2, t1, t2):
                return True
    
    if rect.contains_point(*triangle.a) and rect.contains_point(*triangle.b) and rect.contains_point(*triangle.c):
        return True
    
    corners = [
        (rect.x, rect.y), (rect.x + rect.width, rect.y), (rect.x, rect.y + rect.height), (rect.x + rect.width, rect.y + rect.height)
    ]

    for corner in corners:
        if triangle.contains_point(corner):
            return True
    
    return False

def circle_triangle_intersects(circle, triangle):
    """Вспомогательная функция, проверяет,пересекаются ли круг и треугольник
        
        Args:
            circle (Circle): круг 
            triangle (Triangle): треугольник
        Returns:
            bool : True, если фигуры пересекаются(стороны пересекаются с кругом, центр круга внутри треугольника или вершины треугольника внутри круга), иначе False 
    """
    if triangle.contains_point((circle.center_x, circle.center_y)):
        return True
    
    sides = [
        (triangle.a, triangle.b),
        (triangle.b, triangle.c),
        (triangle.c, triangle.a)
    ]
    for p1, p2 in sides:
        if segment_circle_triangle_intersect(p1, p2, circle):
            return True
        
    for point in (triangle.a, triangle.b, triangle.c):
        if circle.contains_point(*point):
            return True
        
    return False

def segment_circle_triangle_intersect(p1, p2, circle):
    """Вспомогательная функция, проверяет,пересекаются ли отрезок с кругом
        
        Args:
            p1 (tuple): начало отрезка (x, y).
            p2 (tuple): конец отрезка (x, y).
            circle (Circle): круг
        Returns:
            bool : True, если отрезок пересекается с кругом или касается его, иначе False 
    """
    cx, cy = circle.center_x, circle.center_y
    x1, y1 = p1
    x2, y2 = p2
    dx = x2-x1
    dy = y2-y1

    if dx == 0 and dy == 0:
        return circle.contains_point(x1, y1)
    
    a = max(0, min(1, ((cx - x1)*dx + (cy- y1)*dy)/(dx*dx + dy*dy)))
    close_x = x1 + a * dx
    close_y = y1 + a * dy

    hypotenuse = (close_x - cx) ** 2 + (close_y - cy) ** 2
    return hypotenuse <= circle.radius ** 2

def contains(outer, inner):
    """Вспомогательная функция, проверяет,входит ли одна фигура в другую
        
        Args:
            outer: внешняя фигура (Circle, Rectangle или Triangle)
            inner: внутренняя фигура (Circle, Rectangle или Triangle)
        Returns:
            bool : True, если одна фигура находится внутри другой, иначе False 
    """
    if isinstance(outer, Rectangle) and isinstance(inner, Rectangle):
        return outer.contains_rectangle(inner)
    
    if isinstance(outer, Rectangle) and isinstance(inner, Circle):
        return (outer.x <= inner.center_x - inner.radius and outer.y <= inner.center_y - inner.radius and 
                outer.x + outer.width >= inner.center_x + inner.radius and 
                outer.y + outer.height >= inner.center_y + inner.radius)
    
    if isinstance(outer, Rectangle) and isinstance(inner, Triangle):
        return (outer.contains_point(*inner.a) and
                outer.contains_point(*inner.b) and
                outer.contains_point(*inner.c))
    
    if isinstance(outer, Circle) and isinstance(inner, Rectangle):
        corners = [
            (inner.x, inner.y), (inner.x + inner.width, inner.y),
            (inner.x, inner.y + inner.height), (inner.x + inner.width, inner.y + inner.height)
        ]
        return all(outer.contains_point(x, y) for x, y in corners)
            
    if isinstance(outer, Circle) and isinstance(inner, Triangle):
        return (outer.contains_point(*inner.a) and
                outer.contains_point(*inner.b) and
                outer.contains_point(*inner.c))
    
    if isinstance(outer, Triangle):
        
        if isinstance(inner, Rectangle):
            corners = [
                (inner.x, inner.y), (inner.x + inner.width, inner.y),
                (inner.x, inner.y + inner.height), (inner.x + inner.width, inner.y + inner.height)
            ]
            return all(outer.contains_point(p) for p in corners)
        
        if isinstance(inner, Circle):
            return outer.contains_point((inner.center_x, inner.center_y))
        
        if isinstance(inner, Triangle):
            return (outer.contains_point(inner.a) and
                    outer.contains_point(inner.b) and
                    outer.contains_point(inner.c))
        
    return False
