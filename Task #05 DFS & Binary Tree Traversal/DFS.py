#Python Implementation (DFS using Stack)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_stack(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                # Add neighbors in reverse order for correct DFS order
                for neighbor in reversed(self.graph.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)


# Example
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

print("DFS Traversal:")
g.dfs_stack('A')


#Python Implementation (Binary Tree Traversals using OOP)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # Preorder Traversal
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


# Example
tree = BinaryTree('A')
tree.root.left = Node('B')
tree.root.right = Node('C')
tree.root.left.left = Node('D')
tree.root.left.right = Node('E')

print("Preorder Traversal:")
tree.preorder(tree.root)

print("\nInorder Traversal:")
tree.inorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)