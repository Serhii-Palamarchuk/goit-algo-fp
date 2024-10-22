# Завдання 3. Дерева, алгоритм Дейкстри
# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

# критерії оцінювання:
# - Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з використанням бінарної купи (піраміди).
# - У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору вершин 
# та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.

import heapq

# Клас для представлення графу
class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight, bidirectional=True):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))
        if bidirectional:
            if v not in self.edges:
                self.edges[v] = []
            self.edges[v].append((u, weight))

    def get_neighbors(self, node):
        return self.edges.get(node, [])

# Алгоритм Дейкстри для знаходження найкоротшого шляху
class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start):
        # Ініціалізація мінімальної купи (піраміди) для зберігання вершин
        heap = [(0, start)]
        distances = {start: 0}
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            # Проходимо по сусідах поточного вузла
            for neighbor, weight in self.graph.get_neighbors(current_node):
                distance = current_distance + weight

                # Оновлюємо відстань, якщо знайшли коротший шлях
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Основна програма для тестування алгоритму
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == "__main__":
    # Створюємо граф NetworkX для візуалізації
    G = nx.Graph()
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3)
    ]
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)

    # Малюємо граф
    pos = nx.spring_layout(G)  # Розташування вершин графу
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title('Граф для алгоритму Дейкстри')


    # Створюємо граф
    graph = Graph()
    graph.add_edge('A', 'B', 1, bidirectional=True)
    graph.add_edge('A', 'C', 4, bidirectional=True)
    graph.add_edge('B', 'C', 2, bidirectional=True)
    graph.add_edge('B', 'D', 5, bidirectional=True)
    graph.add_edge('C', 'D', 1, bidirectional=True)
    graph.add_edge('D', 'E', 3, bidirectional=True)

    # Виконуємо алгоритм Дейкстри
    dijkstra = Dijkstra(graph)
    start_node = 'A'
    shortest_paths = dijkstra.shortest_path(start_node)

    # Виводимо найкоротші шляхи від початкової вершини до всіх інших
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Відстань до {node}: {distance}")

    plt.show()