"""
    q22.py
    ~~~~~~

    Implement an algorithm to find the kth to last element of a singly
    linked list.

    Hints: #8, #25, #41, #67, #126
"""
from linkedlist import LinkedList

def kth_to_last(ll, k):
    current = runner = ll.head

    # Initalize runner k nodes ahead
    for _ in range(k):
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next
    return current.value


if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    print(kth_to_last(ll, 3))