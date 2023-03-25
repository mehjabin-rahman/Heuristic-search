class Node():
    def __init__(self, state, h_cost, parent=None, g_cost=0, h_cost2=None):
        self.state = state
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.h_cost2 = h_cost2
        self.f_cost = g_cost + h_cost
        if(h_cost2 != None):
            self.f_cost2 = g_cost + h_cost2
        else:
            self.f_cost2 = None

    def get_neighbors(self):
        moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        neighbors = []
        for move in moves:
            neighbor_x = self.state[0]+move[0]
            neighbor_y = self.state[1]+move[1]
            if(neighbor_x < 0 or neighbor_y < 0):
                continue
            neighbors.append((neighbor_x, neighbor_y))
        return neighbors

    def update(self, parent, g_cost, h_cost, h_cost2=None):
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = self.g_cost + self.h_cost
        self.h_cost2 = h_cost2
        if(self.h_cost2 != None):
            self.f_cost2 = self.g_cost + self.h_cost2

    def __eq__(self, node):
        return (self.state == node.state)

    def __lt__(self, node):
        return (self.g_cost<node.g_cost, self.h_cost<node.h_cost, self.f_cost<node.f_cost)

    def status_open(self, value):
        self.in_open = value

    def status_closed(self, value):
        self.in_closed = value

    def __hash__(self):
        pass