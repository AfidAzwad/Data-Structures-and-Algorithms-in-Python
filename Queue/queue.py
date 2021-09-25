''' Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. 
    One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). 
'''
# The order is First In First Out (FIFO). 
# Example: Patient serial in hospital 
# time complexity of enqueue is O(1) cause everytime we are dealing with 1 index
# time complexity of dequeue is O(n) cause everytime we are dealing with 0 index and for this all the elements are rearranging everytime. So for n items it will be O(n)



class queue():
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
