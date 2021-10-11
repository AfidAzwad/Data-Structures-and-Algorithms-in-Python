class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


node1 = Node(2)
node2 = Node(3)
node3 = Node(5)

list1 = LinkedList()
list1.append(2)
list1.append(3)
list1.append(5)
list1.append(9)

print("\nValue of Node 1 :", node1.data)
print("Value of Node 2 :", node2.data)
print("Value of Node 3 :", node3.data)

print("\nLength of the Linked list : ", list1.length(),"\n")

print("Value of 2nd position : ",list1.get_element(1))

list1.show_elements()