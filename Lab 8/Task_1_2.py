def pop_best(open_list):                 # remove and return the node with lowest f
    best = 0
    for i in range(1, len(open_list)):
        if open_list[i][0] < open_list[best][0]:
            best = i
    node = open_list[best]
    del open_list[best]
    return node


class Graph:

    def __init__(self):
        self.adj = {}                    # city -> list of (neighbour, distance)
        self.h = {}                      # city -> straight-line distance to goal

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, v, w, cost):      # road v <-> w with distance cost
        self.add_vertex(v)
        self.add_vertex(w)
        self.adj[v].append((w, cost))
        self.adj[w].append((v, cost))

    def set_h(self, v, value):           # heuristic value of city v
        self.h[v] = value

    def search(self, s, goal, use_g):
        if s not in self.adj:
            print(f"Vertex {s} does not exist in graph.")
            return

        open_list = [[self.h.get(s, 0), 0, s, None]]   # node = [f, g, city, parent]
        closed = []

        while open_list:
            cur = pop_best(open_list)
            city = cur[2]

            if city in closed:
                continue
            closed.append(city)

            if city == goal:                           # rebuild path via parents
                path = []
                n = cur
                while n:
                    path.append(n[2])
                    n = n[3]
                path.reverse()
                print(" -> ".join(path), "| cost =", cur[1])
                return

            for nb, w in self.adj[city]:
                if nb not in closed:
                    g = cur[1] + w               # cost so far to reach this neighbour
                    h = self.h.get(nb, 0)        # estimated distance to the goal
                    if use_g:
                        f = g + h                # A*
                    else:
                        f = h                    # Greedy
                    open_list.append([f, g, nb, cur])

        print("Goal not found")

    def greedy(self, s, goal):           # f = h(n)
        self.search(s, goal, False)

    def astar(self, s, goal):            # f = g(n) + h(n)
        self.search(s, goal, True)


g = Graph()

g.add_edge('Arad', 'Zerind', 75)
g.add_edge('Arad', 'Sibiu', 140)
g.add_edge('Arad', 'Timisoara', 118)
g.add_edge('Zerind', 'Oradea', 71)
g.add_edge('Oradea', 'Sibiu', 151)
g.add_edge('Timisoara', 'Lugoj', 111)
g.add_edge('Lugoj', 'Mehadia', 70)
g.add_edge('Mehadia', 'Dobreta', 75)
g.add_edge('Dobreta', 'Craiova', 120)
g.add_edge('Sibiu', 'Fagaras', 99)
g.add_edge('Sibiu', 'Rimnicu Vilcea', 80)
g.add_edge('Rimnicu Vilcea', 'Craiova', 146)
g.add_edge('Rimnicu Vilcea', 'Pitesti', 97)
g.add_edge('Craiova', 'Pitesti', 138)
g.add_edge('Fagaras', 'Bucharest', 211)
g.add_edge('Pitesti', 'Bucharest', 101)
g.add_edge('Bucharest', 'Giurgiu', 90)
g.add_edge('Bucharest', 'Urziceni', 85)
g.add_edge('Urziceni', 'Hirsova', 98)
g.add_edge('Urziceni', 'Vaslui', 142)
g.add_edge('Hirsova', 'Eforie', 86)
g.add_edge('Vaslui', 'Iasi', 92)
g.add_edge('Iasi', 'Neamt', 87)

g.set_h('Arad', 366)
g.set_h('Bucharest', 0)
g.set_h('Craiova', 160)
g.set_h('Dobreta', 242)
g.set_h('Eforie', 161)
g.set_h('Fagaras', 176)
g.set_h('Giurgiu', 77)
g.set_h('Hirsova', 151)
g.set_h('Iasi', 226)
g.set_h('Lugoj', 244)
g.set_h('Mehadia', 241)
g.set_h('Neamt', 234)
g.set_h('Oradea', 380)
g.set_h('Pitesti', 100)
g.set_h('Rimnicu Vilcea', 193)
g.set_h('Sibiu', 253)
g.set_h('Timisoara', 329)
g.set_h('Urziceni', 80)
g.set_h('Vaslui', 199)
g.set_h('Zerind', 374)

print("Task 1: Greedy Best First")
g.greedy('Arad', 'Bucharest')

print("Task 2: A*")
g.astar('Arad', 'Bucharest')