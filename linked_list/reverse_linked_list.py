# Reverse a Singly Linked List
# This program demonstrates reversing a linked list using an iterative approach

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

    # Reverse the linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

# Test the linked list reverse
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Original Linked List:")
    ll.print_list()

    ll.reverse()

    print("Reversed Linked List:")
    ll.print_list()


# Time Complexity:
# reverse() -> O(n) where n is number of nodes

# Space Complexity:
# O(1) since reversal is done in-place
