# This class represents a single node in a singly linked list.
# Each node contains:
# - val: the actual value/data stored in the node
# - next: a reference (pointer) to the next node in the list
#
# The 'next' parameter defaults to None, meaning:
# - if no next node is provided, this node is the end of the list
# - otherwise, it will point to another ListNode object
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# This function creates a new node and inserts it at the start of the list.
#
# How it works:
# 1. Create a new node with the given value
# 2. Make the new node point to the current head
# 3. Return the new node as the new head of the list
#
# Important concept:
# - The head always represents the start of the linked list
# - By inserting at the beginning, we are shifting the head forward
#
# Example:
# If current list is:
# 2 → 3 → 4 → None
#
# After inserting 1:
# 1 → 2 → 3 → 4 → None
def insert_at_beginning(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node



# This function walks through the linked list from the head to the end.
#
# How it works:
# 1. Start at the head node
# 2. While the current node exists:
#    - print its value
#    - move to the next node using .next
# 3. Stop when we reach None (end of list)
#
# Important concept:
# - Traversal is done using a pointer (current)
# - We DO NOT modify the original head
#
# Example output:
# 1 → 2 → 3 → 4 → 5 → None
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next
    print("None")



# We start with an empty list (head = None)
#
# Then we insert values one by one at the beginning.
# Because we are inserting at the beginning,
# the final order will be reversed from insertion order.
#
# Insert order:
# 5 → 4 → 3 → 2 → 1
#
# Final linked list structure:
# 1 → 2 → 3 → 4 → 5 → None
head = None
head = insert_at_beginning(head, 5)
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)



# This will print all elements in the linked list from head to end.
traverse(head)