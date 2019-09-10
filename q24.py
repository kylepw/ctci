"""
    q24.py
    ~~~~~~
"""
from linkedlist import LinkedList

def partition(ll, value):
    pass

if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)