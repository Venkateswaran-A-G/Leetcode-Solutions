# Date: 07-10-2026
# Problem Number: 876
# Problem Title: Middle of the Linked List
# LeetCode Link: https://leetcode.com/problems/middle-of-the-linked-list/description/
# Difficulty: Easy
# Topic: Slow Fast Pointer Technique
# Time Complexity: O(N)
# Space Complexity: O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

