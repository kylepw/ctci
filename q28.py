"""
    q28.py
    ~~~~~~
    Loop Detection: Given a circular linked list, implement an algorithm that
    returns the node at the beginning of the loop.
    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node's next
    pointer points to an earlier node, so as to make a loop in the linked list.
    EXAMPLE
    Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
    Output: C

    Hints: #50, #69, #83, #90
"""
from linkedlist import LinkedList, LinkedListNode

def loop_detection(ll):
    if ll.tail.next is None:
        return

    current = ll.head
    runner = ll.head.next.next
    while current is not runner:
        current = current.next.next
        runner = runner.next
    return current

def loop_detection_pythonic(ll):
    if ll.tail.next is None:
        return

    stack = []
    node = ll.head
    while node not in stack:
        stack.append(node)
        node = node.next
    return node

if __name__ == '__main__':
    loop_node = LinkedListNode(3)
    ll = LinkedList([1, 2, 0])
    ll.tail.next = loop_node
    ll.tail = ll.tail.next
    ll.add(4)
    ll.tail.next = loop_node
    ll.tail = ll.tail.next
    print(loop_detection(ll))