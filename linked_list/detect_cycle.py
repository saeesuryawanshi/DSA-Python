# Detect Cycle in a Singly Linked List using Floyd's Tortoise and Hare Algorithm
# Approach:
# - Use two pointers (slow and fast)
# - Slow moves one step, fast moves two steps
# - If a cycle exists, they will meet

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
    def print_list(self, limit=20):
        # limit added to prevent infinite loop in case of cycle
        curr = self.head
        count = 0
        while curr and count < limit:
            print(curr.data, end=" -> ")
            curr = curr.next
            count += 1
        if curr:
            print("...")
        else:
            print("None")

    # Detect cycle
    def has_cycle(self):
    """
    Detects whether the linked list contains a cycle
    using Floyd's Tortoise and Hare algorithm
    """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Test the linked list cycle detection
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    # Creating a cycle manually: last node points to second node
    ll.head.next.next.next.next = ll.head.next  

    if ll.has_cycle():
        print("Cycle detected in the linked list")
    else:
        print("No cycle detected")

# Time Complexity:
# O(n) where n is the number of nodes

# Space Complexity:
# O(1) since no extra space is used
