class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        visited = set()
        return self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        result = [vertex]
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                result.extend(self._dfs_recursive(neighbor, visited))
        return result

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([x for x in self.graph.get(vertex, []) if x not in visited])

        return result

def main():
    g = Graph()
    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5),
        (3, 5), (4, 6), (5, 6),
        (6, 7), (5, 7)
    ]

    for u, v in edges:
        g.add_edge(u, v)
        g.add_edge(v, u)  # Assuming the graph is undirected

    start_node = 1
    print("DFS traversal of the graph:")
    print(g.dfs(start_node))

    print("BFS traversal of the graph:")
    print(g.bfs(start_node))

if __name__ == "__main__":
    main()
