def pop(stack):
    last = stack[-1]
    del stack[-1]
    return last


class Graph:

    def __init__(self):
        self.adj = {}

    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []
        if w not in self.adj:
            self.adj[w] = []
        self.adj[v].append(w)

    def ids(self, s, goal, max_depth):
        for limit in range(max_depth + 1):
            print(f"Limit {limit}: ", end="")

            stack = [(s,0)]

            while stack:
                node, depth = pop(stack)
                print(node, end=" ")

                if node == goal:
                    print("\nGoal Found")
                    return

                if depth < limit:
                    for i in reversed(self.adj[node]):
                        stack.append((i,depth+1))

            print()

        print("Goal not found")


g = Graph()

g.add_edge('A','B')
g.add_edge('A','F')
g.add_edge('A','D')
g.add_edge('A','E')
g.add_edge('B','K')
g.add_edge('B','J')
g.add_edge('D','G')
g.add_edge('E','C')
g.add_edge('E','H')
g.add_edge('E','I')
g.add_edge('K','N')
g.add_edge('K','M')
g.add_edge('I','L')

g.ids('A','G',4)