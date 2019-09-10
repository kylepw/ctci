"""
    q21.py
    ~~~~~~

    Remove Dups: Write code to remove duplicates from an unsorted list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?

    Hints: #9, #40
"""

def remove_dups(head):
    """Remove duplicate node values from linked list that starts at `head`."""
    n = head
    vals = set()
    vals.add(n.data)

    while (n.next):
        if n.next.data in vals:
            n.next = n.next.next
        else:
            vals.add(n.next.data)
            n = n.next
    return head

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'Node({self.data})'

def print_list(head):
    n = head
    while n.next != None:
        print(n, '-> ', end='')
        n = n.next
    print(n)

if __name__ == '__main__':
    # Initialize values
    head = Node(data=0)
    n = head
    for data in range(1, 5):
        n.next = Node(data)
        n.next.next = Node(data)
        n = n.next.next
    n.next = Node(data=0)
    n.next.next = Node(data=2)

    print_list(head)
    print('After duplicates removed:')
    print_list(remove_dups(head))