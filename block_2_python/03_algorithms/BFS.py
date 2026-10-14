from collections import deque

graph = {
    "Аня": ["Ваня", "Вика", "Даша"],
    "Ваня": ["Аня", "Глеб", "Егор"],
    "Вика": ["Аня", "Женя", "Зоя"],
    "Глеб": ["Ваня", "Илья"],
    "Даша": ["Аня", "Кира", "Леша"],
    "Егор": ["Ваня", "Маша"],
    "Женя": ["Вика", "Никита"],
    "Зоя": ["Вика", "Оля"],
    "Илья": ["Глеб", "Паша"],
    "Кира": ["Даша", "Рита"],
    "Леша": ["Даша", "Сережа"],
    "Маша": ["Егор", "Таня"],
    "Никита": ["Женя", "Уля"],
    "Оля": ["Зоя", "Федор"],
    "Паша": ["Илья", "Юля"],
    "Рита": ["Кира", "Ян"],
    "Сережа": ["Леша", "Ян"],
    "Таня": ["Маша", "Уля"],
    "Уля": ["Никита", "Таня", "Федор"],
    "Федор": ["Оля", "Уля"],
    "Юля": ["Паша"],
    "Ян": ["Рита", "Сережа"]
}

def bfs(graph, start, goal):
    """
    Сложность поиска:
        O(V+E) : V - количество вершин в графе E - количество ребер в графе
            каждую вершину и каждое ребро просматриваем по одному разу

    """

    if start == goal:
        return [start]
    
    queue = deque([start])
    came_from = {}
    came_from[start] = None

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

                if neighbor == goal:
                    path = []
                    node = goal
                    while node is not None:
                        path.append(node)
                        node = came_from[node]
                    path.reverse()
                    return path
    return None



start = "Ваня"
goal = "Сережа"
path = bfs(graph, start, goal)

if path:
    print(f"Кратчайший путь от {start} до {goal}:")
    print("-".join(path))
    print(f"Количество ребер: {len(path) - 1}")
else:
    print("Путь не найден")
print(len(graph))