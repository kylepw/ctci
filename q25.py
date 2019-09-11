"""
    q25.py
    ~~~~~~
    You have two numbers represented by a linked list, where each node
    contains a single digit. The digits are stored in reverse order, such
    that the 1's digit is at the head of the list. Write a function that
    adds the two numbers and returns the sum as a linked list.
    Example:
    Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.

    Follow up:
    Suppose the digits are stored in forward order. Repeat the above problem.
    Example:
    Input:  (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
    Output: 9 -> 1 -> 2. That is, 912.

    Hints: #7, #30, #71, #95, #109
"""
from linkedlist import LinkedList

def _sum_list(ll):
    sum = 0
    p = 1
    runner = ll.head
    while runner:
        sum += runner.value * p
        p *= 10
        runner = runner.next
    return sum

def _int_to_ll(n):
    """Convert integer to linked list of digits"""
    lst_vals = []
    while n:
        remainder = n % 10
        lst_vals.append(remainder)
        n = (n - remainder) // 10
    return LinkedList(lst_vals)

def sum_lists(ll_a, ll_b):
    sum = _sum_list(ll_a) + _sum_list(ll_b)
    return f'{_int_to_ll(sum)}'

def sum_lists_followup(ll_a, ll_b):
    pass

if __name__ == '__main__':
    ll_a = LinkedList()
    ll_a.generate(4, 0, 9)
    ll_b = LinkedList()
    ll_b.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))
    print(sum_lists_followup(ll_a, ll_b))