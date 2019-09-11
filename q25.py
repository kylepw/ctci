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

def sum_lists_2(ll_a, ll_b):
    """Easy conversion implementation"""
    sum = _sum_list(ll_a) + _sum_list(ll_b)
    return f'{_int_to_ll(sum)}'

def sum_lists(ll_a, ll_b):
    """Better implementation"""
    ll = LinkedList()
    num_a = ll_a.head
    num_b = ll_b.head

    carry = 0
    while num_a or num_b:
        sum = carry
        if num_a:
            sum += num_a.value
            num_a = num_a.next
        if num_b:
            sum += num_b.value
            num_b = num_b.next

        ll.add(sum % 10)
        carry = sum // 10
    if carry:
        ll.add(carry)
    return ll


def sum_lists_followup(ll_a, ll_b):
    ll = LinkedList()

    if len(ll_a) != len(ll_b):
        diff = abs(len(ll_a) - len(ll_b))
        smaller = ll_a if len(ll_a) < len(ll_b) else ll_b
        for _ in range(diff):
            smaller.add_to_beginning(0)

    carry = 0
    for i in reversed(range(len(ll_a))):
        pos_a = ll_a.head
        pos_b = ll_b.head
        for _ in range(i):
            pos_a = pos_a.next
            pos_b = pos_b.next
        sum = pos_a.value + pos_b.value + carry
        ll.add_to_beginning(sum % 10)
        carry = sum // 10

    if carry:
        ll.add_to_beginning(carry)
    return ll

if __name__ == '__main__':
    ll_a = LinkedList()
    ll_a.generate(4, 0, 9)
    ll_b = LinkedList()
    ll_b.generate(3, 0, 9)
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))
    print(sum_lists_followup(ll_a, ll_b))

    ll_a = LinkedList()
    ll_a.add_multiple([9, 7, 8])
    ll_b = LinkedList()
    ll_b.add_multiple([6, 8, 5])
    print(ll_a)
    print(ll_b)
    print(sum_lists(ll_a, ll_b))
    print(sum_lists_followup(ll_a, ll_b))