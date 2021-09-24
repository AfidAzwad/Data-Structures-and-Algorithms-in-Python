# Stack is a linear data structure that serves as a collection of elements,with two main principal operations: 
# Push, which adds an element to the collection, and Pop, which removes 
# the most recently added element that was not yet removed.
# It follows LIFO method

class stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        print(self.items)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False

if __name__== "__main__":
    stk = stack()
    stk.push(0)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.push(6)
  
    print("\nPoping Started : \n")
 
    while not stk.is_empty():
     item = stk.pop()
     print(stk.items)


        