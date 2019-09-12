"""
    q26.py
    ~~~~~~
    Palindrome: Implement a function to check if a linked list is a palindrome.

    Hints: #5, #13, #29, #61, #101
"""
from linkedlist import LinkedList

def is_palindrome(ll):
    stack = []

    runner = ll.head
    while runner:
        stack.append(runner.value)
        runner = runner.next

    runner = ll.head
    while stack and runner:
        if stack.pop() != runner.value:
            return False
        runner = runner.next
    return True

def is_palindrome_solution(ll):
    """Practice given solution"""
    print(ll)
    stack = []

    slow = fast = ll.head
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    return True

if __name__ == '__main__':
    ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
    #print(is_palindrome(ll_true))
    print(is_palindrome_solution(ll_true))
    ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    #print(is_palindrome(ll_false))
    print(is_palindrome_solution(ll_false))