# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue():
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def empty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def put(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def get(self):
        min_val = 0
        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[min_val][0]:
                min_val = i
        item = self.queue[min_val]
        del self.queue[min_val]
        return item