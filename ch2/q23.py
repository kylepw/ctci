"""
    q23.py
    ~~~~~~

    Delete Middle Node: Implement an algorithm to delete a node in the middle
    (i.e., any node but the first and last node, not necessarily the exact
    middle) of a singly linked list, given only access to that node.

    Example:
    Input: the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e->f

    Hints: #72
"""
from linkedlist import LinkedList, LinkedListNode

def delete_middle_node(middle_node):
    if not isinstance(middle_node, LinkedListNode):
        return
    runner = middle_node
    while runner.next.next:
        runner.value = runner.next.value
        runner = runner.next
    runner.value = runner.next.value
    runner.next = None

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)