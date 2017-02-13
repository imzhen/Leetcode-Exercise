#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers
#
# Medium (26.58%)
# Total Accepted:    243404
# Total Submissions: 915852
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        enter = 0
        new_node = ListNode(0)
        result_node = new_node
        while l1 or l2 or enter:
            l1_curr, l2_curr = 0, 0
            if l1:
                l1_curr = l1.val
                l1 = l1.next
            if l2:
                l2_curr = l2.val
                l2 = l2.next
            enter, value = divmod(l1_curr + l2_curr + enter, 10)
            new_node.next = ListNode(value)
            new_node = new_node.next
        return result_node.next
