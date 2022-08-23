# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        cnt = 0
        # 길이찾기
        while node:
            cnt += 1
            # print(first.val, cnt)
            node = node.next
            
        
        node = head
        for i in range(cnt - n - 1):
            #print(node.val)
            node = node.next
        #print(node.val)
        if cnt == 1 and n == 1:
            return head.next
        elif cnt == n:
            head = head.next
            node.next = head.next
        else:
            node.next = node.next.next
        return head