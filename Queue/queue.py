# Queue is an abstract data structure, somewhat similar to Stacks. 
# Unlike stacks, a queue is open at both its ends. One end is always used to 
# insert data (enqueue) and the other is used to remove data (dequeue). 

# The order is First In First Out (FIFO). 
# Example: Patient serial in hospital 

class queue():
    pass
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.append(item)
        print(self.items)

    def dequeue(self):
        return self.items.pop(0)
    
    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__ == "__main__":
    Q = queue()

    for i in range(10):
      Q.enqueue(i)
    
    print("\nDequeuing Started : \n")

    while not Q.is_empty():
        item = Q.dequeue()
        print(Q.items)
