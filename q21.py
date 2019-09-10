"""
    q21.py
    ~~~~~~

    Remove Dups: Write code to remove duplicates from an unsorted list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?

    Hints: #9, #40
"""

def remove_dups(head):
    """Remove duplicate node values from linked list that starts at `head`.

        Runtime: O(N)
    """
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

def remove_dups_run(head):
    """Remove duplicate node values with running pointers.

        Runtime: O(N^2)
    """
    p1 = p2 = head
    while (p1.next):
        p1 = p1.next.next if p1.next.next else p1.next
        p2 = p2.next
    # p1 is at beginning, p2 is beginning of second half
    p1 = head
    

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f'Node({self.data})'

def print_list(head):
    n = head
    while n.next.next:
        print(n, '-> ', end='')
        n = n.next
    print(n)

def init_list():
    """Return head of linked list with values"""
    head = Node(data=0)
    n = head
    for data in range(1, 5):
        n.next = Node(data)
        n.next.next = Node(data)
        n = n.next.next
    n.next = Node(data=0)
    n.next.next = Node(data=2)

    return head

if __name__ == '__main__':
    # Initialize values
    """ head1 = init_list()
    print_list(head1)
    print('After duplicates removed in O(N):')
    print_list(remove_dups(head1)) """

    head2 = init_list()

    print_list(head2)
    print('After duplicates removed in O(N^2): ')
    remove_dups_run(head2)
    #print_list(remove_dups_run(head2))