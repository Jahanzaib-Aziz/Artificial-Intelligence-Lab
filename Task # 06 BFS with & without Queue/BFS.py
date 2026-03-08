# BFS without Queue & without Node
class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):

        visited = []
        bfs_order = []

        temp_list = []
        temp_list.append(start)

        visited.append(start)

        while len(temp_list) != 0:

            current = temp_list[0]
            temp_list.pop(0)

            bfs_order.append(current)

            if current in self.graph:
                for neighbour in self.graph[current]:

                    if neighbour not in visited:
                        visited.append(neighbour)
                        temp_list.append(neighbour)

        print("BFS Traversal:", bfs_order)


g = Graph()

g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("B","E")
g.add_edge("C","F")

g.bfs("A")
# BFS with Queue
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):

        visited = []
        q = Queue()

        visited.append(start)
        q.enqueue(start)

        while not q.is_empty():

            node = q.dequeue()
            print(node, end=" ")

            if node in self.graph:
                for neighbour in self.graph[node]:

                    if neighbour not in visited:
                        visited.append(neighbour)
                        q.enqueue(neighbour)


g = Graph()

g.add_edge("A","B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("B","E")
g.add_edge("C","F")

print("BFS Traversal:")
g.bfs("A")