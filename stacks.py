class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    

class Stacks:
    def __init__(self):
        self.first = None
        self.latest = None
        self.length = 0
        
        
    def push(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.first = new_node
            self.latest = new_node
        else:
            existing_latest_node = self.latest
            self.latest = new_node
            new_node.next = existing_latest_node
        self.length += 1
        return self.length
    
    
    def pop_from_beginnig(self):
        current = self.latest
        if self.length == 0:
            print("There is no node")
        else:
            self.latest = current.next
            current = current.next
            self.length -= 1
        return current
    

    def print_nodes(self):
        current = self.latest
        while current:
            print(current.value, end=" <-- ")
            current = current.next
        print("NONE")
        print(self.length)
        
            
            
stacked_data = Stacks()
stacked_data.print_nodes()

stacked_data.push('first')
stacked_data.print_nodes()
stacked_data.push('second')
stacked_data.print_nodes()
stacked_data.push('latest')
stacked_data.print_nodes()
            

stacked_data.pop_from_beginnig()
stacked_data.print_nodes()
stacked_data.pop_from_beginnig()
stacked_data.print_nodes()
stacked_data.pop_from_beginnig()
stacked_data.print_nodes()
