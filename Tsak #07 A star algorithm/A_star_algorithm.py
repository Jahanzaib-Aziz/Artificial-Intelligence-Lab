# Simple A* Algorithm using Python OOP

class Graph:
    def __init__(self):
        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'D': 2, 'E': 5},
            'C': {'F': 3},
            'D': {},
            'E': {'G': 2},
            'F': {'G': 1},
            'G': {}
        }

        # Heuristic values
        self.h = {
            'A': 7,
            'B': 6,
            'C': 4,
            'D': 5,
            'E': 2,
            'F': 1,
            'G': 0
        }

    def astar(self, start, goal):
        open_list = [start]
        g = {start: 0}
        parent = {start: None}

        while open_list:
            current = min(open_list, key=lambda x: g[x] + self.h[x])

            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            open_list.remove(current)

            for neighbor in self.graph[current]:
                cost = g[current] + self.graph[current][neighbor]

                if neighbor not in g or cost < g[neighbor]:
                    g[neighbor] = cost
                    parent[neighbor] = current
                    open_list.append(neighbor)

        return None


g = Graph()
result = g.astar('A', 'G')

print("Shortest Path:", result)