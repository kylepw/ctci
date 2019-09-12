"""
    q27.py
    ~~~~~~
    Given two (singly) linked lists, determine if the two lists intersect.
    Return the intersecting node. Note that the intersection is defined
    based on reference, not value. That is, if the kth node of the first
    linked list is the exact same node (by reference) as the jth node of
    the second linked list, then they are intersecting.

    Hints: #20, #45, #55, #65, #76, #93, #111, #120, #129
"""
from linkedlist import LinkedList, LinkedListNode

def intersection(ll_a, ll_b):
    len_a = len(ll_a)
    len_b = len(ll_b)
    diff = abs(len_a - len_b)
    if diff > 0:
        shorter = ll_a if len_a < len_b else ll_b

        for _ in range(diff):
            shorter.add_to_beginning(0)
    a = ll_a.head
    b = ll_b.head
    intersect_pt = False
    while a or b:
        intersect_pt = a if a is b else intersect_pt
        a = a.next
        b = b.next
    return intersect_pt

def intersection_solution(ll_a, ll_b):
    if ll_a.tail is not ll_b.tail:
        return False

    longer = ll_a if len(ll_a) > len(ll_b) else ll_b
    shorter = ll_b if len(ll_b) < len(ll_a) else ll_a

    s_node, l_node = shorter.head, longer.head
    diff = len(longer) - len(shorter)
    for _ in range(diff):
        l_node = l_node.next

    while s_node is not l_node:
        s_node = s_node.next
        l_node = l_node.next

    return l_node

if __name__ == '__main__':
    shared_node = LinkedListNode(value=5)

    ll_a = LinkedList([1, 2, 3, 4])
    ll_a.tail.next = shared_node
    ll_a.tail = ll_a.tail.next

    ll_b_true = LinkedList([6, 7, 13, 8, 9])
    ll_b_true.tail.next = shared_node
    ll_b_true.tail = ll_b_true.tail.next
    print(ll_a)
    print(ll_b_true)
    #print(intersection_solution(ll_a, ll_b_true))
    print(intersection(ll_a, ll_b_true))

    ll_b_false = LinkedList([6, 7, 11, 3, 8, 9, 5])
    print(ll_b_false)
    #print(intersection_solution(ll_a, ll_b_false))
    print(intersection(ll_a, ll_b_false))