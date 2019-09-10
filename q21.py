"""
    q21.py
    ~~~~~~

    Remove Dups: Write code to remove duplicates from an unsorted list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?

    Hints: #9, #40
"""
from linkedlist import LinkedList

def remove_dups(ll):
    """Remove duplicate node values from linked list that starts at `head`.

        Runtime: O(N)
    """
    n = ll.head
    vals = set([n.value])

    while n.next:
        if n.next.value in vals:
            n.next = n.next.next
        else:
            vals.add(n.next.value)
            n = n.next
    return ll.head

def remove_dups_run(ll):
    """Remove duplicate node values with running pointers.

        Runtime: O(N^2)
    """
    p1 = p2 = ll.head
    while p1.next:
        p1 = p1.next.next if p1.next.next else p1.next
        p2 = p2.next
    # p1 is at beginning, p2 is beginning of second half
    p1 = ll.head

if __name__ == '__main__':
    ll = LinkedList()
    """
    ll.generate(100, 0, 9)
    print('Original: ')
    print(ll)
    remove_dups(ll)
    print('After duplicates removed in O(N):')
    print(ll) """

    ll.generate(100, 0, 9)
    print('Original: ')
    print(ll)
    remove_dups_run(ll)
    print('After duplicates removed in O(N^2):')
    print(ll)