import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node

# Function to convert a binary heap into a binary tree structure
def heap_to_tree(heap):
    if not heap:
        return None
    
    nodes = [Node(val) for val in heap]
    
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    
    return nodes[0]

# Function to add edges to the graph recursively
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store node value
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

# Function to draw the binary tree with updated colors
def draw_tree(tree_root, node_colors):
    if not tree_root:
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node_colors.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use node value for labels

    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    nx.draw(tree, pos=pos, labels=labels, ax=ax, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Function to perform depth-first traversal and visualize each step
def depth_first_traversal(tree_root):
    if not tree_root:
        return

    stack = [tree_root]
    visited = set()
    step = 0
    node_colors = {}

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            # Assign color based on traversal order
            color_intensity = hex(255 - step * 10)[2:].zfill(2)
            node_colors[node.id] = f"#{color_intensity}{color_intensity}FF"
            step += 1
            draw_tree(tree_root, node_colors)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

# Function to perform breadth-first traversal and visualize each step
def breadth_first_traversal(tree_root):
    if not tree_root:
        return

    queue = deque([tree_root])
    visited = set()
    step = 0
    node_colors = {}

    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            # Assign color based on traversal order
            color_intensity = hex(255 - step * 10)[2:].zfill(2)
            node_colors[node.id] = f"#{color_intensity}{color_intensity}FF"
            step += 1
            draw_tree(tree_root, node_colors)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Example usage
heap = [10, 5, 3, 2, 4]
tree_root = heap_to_tree(heap)

print("Depth-First Traversal Visualization:")
depth_first_traversal(tree_root)

print("Breadth-First Traversal Visualization:")
breadth_first_traversal(tree_root)
