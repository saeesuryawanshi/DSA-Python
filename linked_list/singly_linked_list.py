# Implementation of Singly Linked List
# Each node contains data and a reference to the next node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Print the linked list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Test the linked list
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Linked List:")
    ll.print_list()

# Time Complexity:
# append() -> O(n) because we traverse the list
# print_list() -> O(n)

# Space Complexity:
# O(1) extra space (excluding the linked list storage)
