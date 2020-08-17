""" 
Data structure used for implementing search agents 
"""
import heapq
"""
Utility Name : Stack 
Utility Description :
    stack is used to stor elements, based on list it's stratigy
    is last in first out (LIFO).
"""
class Stack(object):
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()
    
    def isEmpty(self):
        # return False if len(this.list)==0 else True
        return len(self.list)==0
    

class Queue(object):
    """ FIFO """
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        item = self.list[0]
        self.list.remove(self.list[0])
        return item
    
    def isEmpty(self):
        return len(self.list) == True


class PriorityQueue(object):

    def __init__(self):
        self.heap = []
        self.count = 0 
    
    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1
    
    def pop(self):
        heapq.heapify(self.heap)
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty():
        return len(self.heap)==0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

