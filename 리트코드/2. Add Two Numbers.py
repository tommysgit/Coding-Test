# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = ''
        num2 = ''
        # l1 to digit
        node = l1
        while node:
            num1 += str(node.val)
            node = node.next
        # l2 to digit
        node = l2
        while node:
            num2 += str(node.val)
            node = node.next
        sum_number = int(num1[::-1]) + int(num2[::-1])
        sum_number = str(sum_number)[::-1]
        # 노드 초기화
        node = ListNode(int(sum_number[0]))
        head = node
        for i in range(1, len(sum_number)):
            num = int(sum_number[i])
            node.next = ListNode(num)
            node = node.next
        return head
        
            