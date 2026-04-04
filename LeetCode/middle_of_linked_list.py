def find_middle_node(head):
    slow = head
    fast = head
    while fast != None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    print("None")
    return slow