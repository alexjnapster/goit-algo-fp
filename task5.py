import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def insert_heap(root, val):
    new_node = Node(val)
    q = [root]
    while q:
        temp = q.pop(0)
        if not temp.left:
            temp.left = new_node
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = new_node
            break
        else:
            q.append(temp.right)
    return root

def build_heap(elements):
    if not elements:
        return None
    root = Node(elements[0])
    for element in elements[1:]:
        root = insert_heap(root, element)
    return root

def generate_colors(n):
    base_color = mcolors.hex2color("#1296F0")
    colors = []
    if n == 1:
        colors.append(mcolors.rgb2hex(base_color))
    else:
        for i in range(n):
            factor = 0.1 + 0.9 * (i / (n - 1))
            colors.append(mcolors.rgb2hex([min(1, base_color[j] * factor) for j in range(3)]))
    return colors

def depth_first_traversal(node, visited=None, colors=None):
    if visited is None:
        visited = []
    if colors is None:
        colors = generate_colors(len(visited) + 1)
    if node:
        if len(colors) <= len(visited):
            colors = generate_colors(len(visited) + 1)
        node.color = colors[len(visited)]
        visited.append(node)
        depth_first_traversal(node.left, visited, colors)
        depth_first_traversal(node.right, visited, colors)
    return visited

def breadth_first_traversal(root):
    visited = []
    queue = [root]
    colors = generate_colors(len(queue) + 1)
    while queue:
        node = queue.pop(0)
        if len(colors) <= len(visited):
            colors = generate_colors(len(visited) + 1)
        node.color = colors[len(visited)]
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

elements = [0, 4, 5, 10, 1, 3]
heap_root = build_heap(elements)
dfs_visited = depth_first_traversal(heap_root)
draw_tree(heap_root)
heap_root = build_heap(elements)
bfs_visited = breadth_first_traversal(heap_root)
draw_tree(heap_root)