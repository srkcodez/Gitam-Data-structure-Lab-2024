import heapq  # To implement priority queue


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
        if from_node in self.edges:
            self.edges[from_node].append((to_node, weight))
        else:
            self.edges[from_node] = [(to_node, weight)]

    def dijkstra(self, start):
        # Distance table, store the minimum distance to each node
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0
        # Priority queue to hold nodes to be processed, initialized with start node
        priority_queue = [(0, start)]

        while priority_queue:
            # Get the node with the smallest distance
            current_distance, current_node = heapq.heappop(priority_queue)

            # Nodes can only be added once to the queue
            if current_distance > distances[current_node]:
                continue

            # Process each adjacent node
            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def main():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 3, 1)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 3, 2)

    start_node = 1
    distances = g.dijkstra(start_node)
    print(f"Shortest distances from node {start_node}:")
    for node, distance in distances.items():
        print(f"Distance to node {node}: {distance}")


if __name__ == "__main__":
    main()
