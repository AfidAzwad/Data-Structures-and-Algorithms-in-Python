''' Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over 
    list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides 
    an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
'''
# The order is First In First Out (FIFO). 


from collections import deque

items = deque()
size = int(input("Queue size: "))

print("\nEnqueuing Started : \n")
for i in range(size):
  items.append(i)
  print(items)
    
print("\nDequeuing Started : \n")
for i in range(size):
  items.popleft()
  print(items)
