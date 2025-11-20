# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2=""
        while l1!=None:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        while l2!=None:
            s2 = s2+str(l2.val)
            l2 = l2.next
        s1=s1[::-1]
        s2=s2[::-1]
        sum1 = int(s1)+int(s2)
        sum2 = str(sum1)
        sum2=sum2[::-1]
        head = ListNode(int(sum2[0]),None)
        current = head
        for i in sum2[1:]:
            current.next = ListNode(int(i),current.next)
            current = current.next
        return head
        
