from turtle import home


class Queue:
    def __init__(self):   #initialize the constructor method
        self.queue = list()

    # check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # add an element to the queue
    def enqueue(self, data):
        # insert method to add element
        self.queue.insert(0, data)
        return True

    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return ("Queue is empty!")
        return self.queue.pop()

    # get the size of the queue
    def size(self):
        return len(self.queue)

    # display the queue
    def display(self):
        return self.queue

# create a Queue object
q = Queue()

# insert elements to the queue
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
#q.enqueue('home')

# display the queue
print(q.display())

# remove an element from the queue
print(q.dequeue())

# display the queue
print(q.display())

# check the size of the queue
print(q.size())

# check if the queue is empty
print(q.isEmpty())