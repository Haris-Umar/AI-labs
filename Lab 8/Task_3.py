START = [1, 2, 3,
         5, 6, 0,
         7, 8, 4]

GOAL = [1, 2, 3,
        5, 8, 6,
        0, 7, 4]


def heuristic(state):
    # count misplaced tiles (blank not counted)
    count = 0
    i = 0
    while i < 9:
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
        i += 1
    return count


def find_blank(state):
    i = 0
    while state[i] != 0:
        i += 1
    return i


def neighbours(state):
    result = []
    blank = find_blank(state)
    row = blank // 3
    col = blank % 3

    targets = []
    if row > 0:
        targets.append(blank - 3)  # up
    if row < 2:
        targets.append(blank + 3)  # down
    if col > 0:
        targets.append(blank - 1)  # left
    if col < 2:
        targets.append(blank + 1)  # right

    for t in targets:
        new = state[:]  # copy
        new[blank] = new[t]
        new[t] = 0
        result.append(new)

    return result


def astar():
    # each item: [f, g, state, path]
    open_list = [[heuristic(START), 0, START, [START]]]
    closed = []

    while open_list:
        # pick the item with the lowest f
        best = open_list[0]
        for item in open_list:
            if item[0] < best[0]:
                best = item

        # remove it from open_list
        remaining = []
        for item in open_list:
            if item is not best:
                remaining.append(item)
        open_list = remaining

        g = best[1]
        state = best[2]
        path = best[3]

        if state == GOAL:
            return path, g

        if state in closed:
            continue
        closed.append(state)

        for n in neighbours(state):
            if n not in closed:
                open_list.append([g + 1 + heuristic(n), g + 1, n, path + [n]])

    return None, 0


def show(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


path, moves = astar()

if path:
    print("Solution found!\n")
    for step in path:
        show(step)
    print("Total moves:", moves)
else:
    print("Goal not found!")