class LRUQ(object):

    def __init__(self, max_size, current_size):
        self.max_size = max_size
        self.current_size = current_size
        self.first = None #head of queue (pop from head)
        self.last = None #tail of queue (add to the tail)

    class Node(object):

        def __init__(self, value, child_pointer):
            self.value = value
            self.child_pointer = child_pointer


    def push(self, value):

        newNode = Node(value, None)
        
        if self.first is None: #empty queue
            self.first = newNode
            self.last = newNode
            self.last.child_pointer = None
        
        else:
            self.last.child_pointer = newNode
            self.last = newNode
        
        self.current_size += 1
        if self.current_size > self.max_size:
            to_pop = self.first
            self.first = to_pop.child_pointer #pops the first and moves the queue up
            self.current_size -= 1

    def pop(self):
        if self.first is not None:
            to_pop = self.first
            self.first = to_pop.child_pointer
            self.current_size -= 1
            if self.current_size == 0:
                self.first = None
                self.last = None
            return to_pop.value

        return None

    def make_list(self):
        # result = []
        # while self.current_size > 0:
        #     result.append(self.pop())
        # return result
        
        result = []
        length = self.current_size
        node = self.first
        while length > 0:
            result.append(node.value)
            node = node.child_pointer
            length -= 1
        return result




