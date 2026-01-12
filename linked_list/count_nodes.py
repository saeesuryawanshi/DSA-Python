# Count number of nodes in a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def count_nodes(self):
        """
        Returns the number of nodes in the linked list
        """
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

# Test the linked list
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    print("Number of nodes:", ll.count_nodes())

# Time Complexity: O(n)
# Space Complexity: O(1)
