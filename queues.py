class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queues():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    # def append(self, value):
    def enqueue(self, value):
        new_node = Node(value)
        
        if not self.last:
            self.first = new_node
            self.last = new_node
        else:            
            existing_last_node = self.last
            existing_last_node.next = new_node
            self.last = new_node
        self.length += 1
    
    
    def dequeue(self):
        if not self.first:
            return None
        else:
            existing_first_node = self.first
            self.first = existing_first_node.next
            existing_first_node.next = None
            self.length -= 1
        
        
    def print_nodes(self):
        current = self.first
        while current:
            print(current.value, end=" --> ")
            current = current.next
        print("NONE")
        print(self.length)
        
    

new_queue = Queues()

new_queue.enqueue('first')    
new_queue.print_nodes()
new_queue.enqueue('second')
new_queue.print_nodes()
new_queue.enqueue('third')
new_queue.enqueue('fourth')

new_queue.print_nodes()

new_queue.dequeue()
new_queue.print_nodes()
new_queue.dequeue()
new_queue.print_nodes()    
new_queue.dequeue()
new_queue.print_nodes()    
new_queue.dequeue()
new_queue.print_nodes()    
  