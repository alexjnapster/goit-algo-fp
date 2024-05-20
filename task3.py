import heapq


def dijkstra(graph, start_vertex):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    # Відстань до початкової вершини дорівнює 0
    distances[start_vertex] = 0
    # Пріоритетна черга для зберігання вершин для обробки
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        # Вибір вершини з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Перевірка чи знайдена краща відстань
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней до сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдена коротша відстань, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Приклад використання
if __name__ == "__main__":
    # Створення графа як словника
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    # Обчислення найкоротших шляхів від початкової вершини до всіх інших
    shortest_paths = dijkstra(graph, start_vertex)

    # Вивід результатів користувачу
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до вершини {vertex}: {distance}")