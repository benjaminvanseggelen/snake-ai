from generic import Space


class Node:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.f = 0
        self.h = 0


class AI:
    @staticmethod
    def search(w: int, h: int, s_x: int, s_y: int, f_x: int, f_y: int, occupied_spaces: list[Space]) -> Space:
        # Initialize nodes
        open_spaces = [[True for i in range(0, w)] for j in range(0, h)]

        for space in occupied_spaces:
            open_spaces[space.y][space.x] = False

        start_node = Node(s_x, s_y)
        open_list = [start_node]
        closed_list: list[Node] = []

        while len(open_list) > 0:
            # Find node with min f
            min_f = 99999
            qi = -1
            for i in range(len(open_list)):
                if open_list[i].f <= min_f:
                    min_f = open_list[i].f
                    qi = i

            q = open_list.pop(qi)

            successors: list[Node] = []
            if q.y > 0 and open_spaces[q.y - 1][q.x]:
                successors.append(Node(q.x, q.y - 1))
            if q.y < h - 1 and open_spaces[q.y + 1][q.x]:
                successors.append(Node(q.x, q.y + 1))
            if q.x > 0 and open_spaces[q.y][q.x - 1]:
                successors.append(Node(q.x - 1, q.y))
            if q.x < w - 1 and open_spaces[q.y][q.x + 1]:
                successors.append(Node(q.x + 1, q.y))

            for successor in successors:
                if successor == None:  # Obstacle
                    continue

                successor.parent = q

                if successor.x == f_x and successor.y == f_y:
                    path: list[Space] = []
                    current = successor
                    while current is not start_node:
                        path.append(Space(current.x, current.y))
                        current = current.parent
                    return path[-1]
                else:
                    successor.g = q.g + 1
                    successor.h = abs(successor.x - f_x) + \
                        abs(successor.y - f_y)
                    successor.f = successor.g + successor.h

                    skip = False
                    for node in closed_list:
                        if node.x == successor.x and node.y == successor.y:
                            skip = True
                            break
                    if skip:
                        continue
                    for node in open_list:
                        if node.x == successor.x and node.y == successor.y and node.g < successor.g:
                            skip = True
                            break
                    if skip:
                        continue

                    open_list.append(successor)
            closed_list.append(q)

        # No possible path
        if len(closed_list) > 1:
            return Space(closed_list[1].x, closed_list[1].y)
        else:
            return Space(closed_list[0].x, closed_list[0].y)
