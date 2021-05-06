# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'ListNode({self.val!r}, {self.next!r})'


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a: int = self.list_to_num(l1)
        b: int = self.list_to_num(l2)
        c: int = a + b
        return self.num_to_list(c)

    @staticmethod
    def list_to_num(node: ListNode) -> int:
        digits = ""
        current: ListNode = node
        while current.next:
            digits = str(current.val) + digits
            current = current.next
        digits = str(current.val) + digits
        return int(digits)

    @staticmethod
    def num_to_list(n: int) -> ListNode:
        digits = list(str(n))
        nodes = [ListNode(val=int(d)) for d in digits]
        for i in range(len(nodes)-1, 0, -1):
            nodes[i].next = nodes[i-1]
            # print(f'{i}: {nodes}')
        return nodes[-1]

