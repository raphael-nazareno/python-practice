class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_at_beginning(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node


def find_middle_node(head):
    slow = head
    fast = head
    while fast != None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    print("None")
    return slow

head = None
head = insert_at_beginning(head, 5)
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)



# This will print all elements in the linked list from head to end.
