import networkx as nx
import heapq

# Create a graph using NetworkX
graph = nx.DiGraph()

# Add edges to the graph
graph.add_weighted_edges_from([
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
])

# Dijkstra's algorithm using NetworkX
def dijkstra(graph, start):
    # Initialize the heap and distances dictionary
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Example usage
distances = dijkstra(graph, 'A')
print("Shortest distances from A:", distances)
