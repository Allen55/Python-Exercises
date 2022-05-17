
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode):
        prev, curr = None, head

        while curr:
            nxt = curr.next  # temp variable
            curr.next = prev
            prev = curr
            curr = nxt

        return prev



list_head = [1, 2, 3, 4, 5] # -> [5,4,3,2,1]

print(reverse_list(list_head))