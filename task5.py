# Завдання 5. Візуалізація обходу бінарного дерева
# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
# Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
# Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
# Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
# 👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, highlight_node=None, title="Binary Tree Visualization"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = ["#1296F0" if node[0] == highlight_node else node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.suptitle(title)
    plt.show()


def build_heap(arr):
    # Функція для побудови бінарної купи з масиву
    if not arr:
        return None

    nodes = [Node(key) for key in arr]
    n = len(nodes)

    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]

    return nodes[0]


def visualize_dfs(tree_root):
    stack = [tree_root]
    visited = set()
    step = 0

    while stack:
        current = stack.pop()
        if current.id not in visited:
            visited.add(current.id)
            # Зміна кольору вузла в залежності від порядку відвідування
            current.color = "#" + format(255 - step * 15, '02x') * 3
            step += 1
            draw_tree(tree_root, highlight_node=current.id, title="Depth-First Search (DFS) Visualization")

            # Додавання дочірніх елементів у стек (правий спочатку, щоб лівий був зверху)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


def visualize_bfs(tree_root):
    queue = deque([tree_root])
    visited = set()
    step = 0

    while queue:
        current = queue.popleft()
        if current.id not in visited:
            visited.add(current.id)
            # Зміна кольору вузла в залежності від порядку відвідування
            current.color = "#" + format(255 - step * 15, '02x') * 3
            step += 1
            draw_tree(tree_root, highlight_node=current.id, title="Breadth-First Search (BFS) Visualization")

            # Додавання дочірніх елементів у чергу (лівий потім правий)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


# Приклад побудови купи
heap_array = [0, 4, 1, 5, 10, 3]
root = build_heap(heap_array)

# Візуалізація обходу в глибину
visualize_dfs(root)

# Візуалізація обходу в ширину
visualize_bfs(root)
