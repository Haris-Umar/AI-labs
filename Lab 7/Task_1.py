def pop(stack):
    last = stack[-1]
    del stack[-1]
    return last


class Graph:

    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, v, w):
        self.add_vertex(v)
        self.add_vertex(w)

        if w not in self.adj[v]:
            self.adj[v].append(w)

    def dls(self, s, goal, limit):
        if s not in self.adj:
            print(f"Vertex {s} does not exist in graph.")
            return

        visited = []
        stack = [(s, 0)]         

        while stack:
            node, depth = pop(stack)

            if node in visited:
                continue

            visited.append(node)
            print(node, end=" ")

            if node == goal:
                print()
                print(f"Goal Found: {node} at depth {depth}")
                return

            if depth < limit:
                for i in reversed(self.adj[node]):
                    if i not in visited:
                        stack.append((i, depth + 1))

        print()
        print(f"Goal not found in depth limit {limit}")


g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('D', 'G')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('I', 'L')

# g.dls('A', 'G', 2)
g.dls('A', 'G', 3)