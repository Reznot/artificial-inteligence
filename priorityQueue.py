import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return bool(len(self.elements) == 0)

    def push(self, item):  # TODO potem to zmodyfikuj jeszcze
        if self.isEmpty():
            self.elements.append(item)
        else:
            i = 0
            contains = False

            while not contains and i < len(self.elements):
                if item.f_cost < self.elements[i].f_cost:
                    self.elements.insert(i, item)
                    contains = True
                else:
                    i += 1
            if not contains:
                self.elements.append(item)
        # heapq.heappush(self.elements, (priority, item))

    def pop(self):  # czy na pewno zwraca Node czy nie tuple/
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.elements.pop(0)         # heapq.heappop(self.elements)[1]

    def pop_last(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.elements.pop(len(self.elements - 1))         # heapq.heappop(self.elements)[1]
