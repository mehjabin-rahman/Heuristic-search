import heapq as hq


# Needs an anytime heap with another heap
class Open():
    def __init__(self):
        self.heap = []

    def __len__(self):
        return (len(self.heap))

    def insert(self, node):
        hq.heappush(self.heap, (node.f_cost, node))

    def anytime_insert(self, node):
        hq.heappush(self.heap, (node.f_cost2, node))

    def next(self):
        best = hq.heappop(self.heap)
        if (len(self.heap) > 0):
            temp = hq.heappop(self.heap)
            while (temp[0] == best[0]):
                if (temp[1].h_cost < best[1].h_cost):
                    hq.heappush(self.heap, best)
                    best = temp
                    temp = hq.heappop(self.heap)
                else:
                    break
            hq.heappush(self.heap, temp)
        return best[1]

    def anytime_next(self):
        best = hq.heappop(self.heap)
        if (len(self.heap) > 0):
            temp = hq.heappop(self.heap)
            while (temp[0] == best[0]):
                if (temp[1].h_cost2 < best[1].h_cost2):
                    hq.heappush(self.heap, best)
                    best = temp
                    temp = hq.heappop(self.heap)
                else:
                    break
            hq.heappush(self.heap, temp)
        return best[1]

    def get_error(self, node):
        flag = 0
        for key in self.heap:
            if (flag == 0):
                min_f_node = key[1]
                flag = 1
                continue
            if ((key[1] < min_f_node)[2]):
                min_f_node = key[1]
        error = node.f_cost - min_f_node.f_cost
        return error

    def test_membership(self, node):
        for key in self.heap:
            if (node == key[1]):
                return (True, key[1])
        return (False, None)