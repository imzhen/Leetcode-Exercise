#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
#
# Medium (32.33%)
# Total Accepted:    164909
# Total Submissions: 506199
# Testcase Example:  '[1]\n1'
#
# Given a linked list, remove the nth node from the end of list and return its
# head.
#
#
# For example,
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
#
#
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        first_head = start
        another_head = start
        while n > 0:
            first_head = first_head.next
            n -= 1
        while first_head.next:
            first_head = first_head.next
            another_head = another_head.next
        another_head.next = another_head.next.next
        return start.next
