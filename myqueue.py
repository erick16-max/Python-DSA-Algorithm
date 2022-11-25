#Queue algorithmn to for First in First out(FIFO)
class Queue:
    def __init__(self):
        self.queue = list()
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def push(self, item):
        return self.queue.append(item)
    
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[len(self.queue) - 1]
        return None
    def the_queue(self):
        return self.queue

new_queue = Queue()
new_queue.push(2)
new_queue.push(3)
print(new_queue.the_queue())