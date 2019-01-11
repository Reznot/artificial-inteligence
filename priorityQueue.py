import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return bool(len(self.elements) == 0)

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):#moze nie dzialac/ TODO jezeli nie dziala to sam zaimplementuj push
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return heapq.heappop(self.elements)
