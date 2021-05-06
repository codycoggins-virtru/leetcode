import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val!r}, {self.next!r})'

    def __str__(self):
        s: List = self.to_list()
        return f'{s}'

    def to_list(self) -> List:
        s: List = []
        pointer = self
        while pointer:
            s.append(pointer.val)
            pointer = pointer.next
        return s

    @staticmethod
    def from_list(nums: List[int]):
        if not nums:
            return None
        nodes = [ListNode(val=i) for i in nums]
        for i in range(0, len(nodes)-1):
            nodes[i].next = nodes[i+1]
        print(f'list_to_nodes: {str(nodes)}')
        return nodes[0]


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result: ListNode = ListNode(-1)
        tail: ListNode = result

        while l1 or l2:
            if not l1:
                tail.next = l2
                tail = l2
                l2 = l2.next
                return result.next

            if not l2:
                tail.next = l1
                tail = l1
                l1 = l1.next
                return result.next

            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next

            else:
                tail.next = l2
                tail = l2
                l2 = l2.next

        return result.next


class MyTestCase(unittest.TestCase):
    def test_mergeTwoLists(self):
        s = Solution()
        testcases = [
            [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]],
            [[], [], []],
            [[], [1, 2], [1, 2]],
            [[1, 3, 5], [], [1, 3, 5]],
            [[1, 1, 1], [10, 11, 12], [1, 1, 1, 10, 11, 12]]
        ]
        for t in testcases:
            l1: ListNode = ListNode.from_list(t[0])
            l2: ListNode = ListNode.from_list(t[1])
            expected: List = t[2]
            print(f'Test Case: {t}')
            result: ListNode = s.mergeTwoLists(l1, l2)
            print(f'  Result: {result}')
            if result:
                result_list: List = result.to_list()
            else:
                result_list: List = []
            self.assertEqual(expected, result_list)


if __name__ == '__main__':
    unittest.main()
