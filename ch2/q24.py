"""
    q24.py
    ~~~~~~

    Write code to partition a linked list around a value, x such that all
    nodes less than x come before all nodes greater than or equal to x. If x
    is contained within the list, the values of x only need to be after the
    elements less than x. The partition element x can appear anywhere in the
    "right partition". It does not need to appear between the left and right
    partitions.

    Example:
    Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

    Hints: #3, #24
"""
from linkedlist import LinkedList, LinkedListNode

def partition(ll, value):
    runner = ll.head
    while runner:
        if runner.next and runner.next.value < value:
            old_head = ll.head
            new_head = runner.next
            runner.next = runner.next.next
            ll.head = new_head
            ll.head.next = old_head
        else:
            runner = runner.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)