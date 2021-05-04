import unittest
from AddTwoNumbers import Solution, ListNode


class MyTestCase(unittest.TestCase):
    def test_ListNode(self):
        a = ListNode(val=1)
        b = ListNode(val=2, next=a)
        self.assertIs(a, b.next)

    def test_list_to_num(self):
        s = Solution()
        a = ListNode(val=1)
        b = ListNode(val=2, next=a)
        self.assertIs(12, s.list_to_num(b))

    def test_num_to_list(self):
        s = Solution()
        num = 123
        nlist: ListNode = s.num_to_list(num)
        self.assertEqual(nlist.val, 3)
        self.assertEqual(nlist.next.val, 2)
        self.assertEqual(nlist.next.next.val, 1)

    def test_addTwoNumbers(self):
        s = Solution()
        self.check_result(123, 456, s)
        self.check_result(243, 564, s)
        self.check_result(0, 1, s)
        self.check_result(7, 1, s)
        self.check_result(9090, 1, s)
        self.check_result(-9090, -1, s)
        self.check_result(0, 0, s)

    def check_result(self, a, b, s):
        c = s.addTwoNumbers(s.num_to_list(a),
                            s.num_to_list(b))
        self.assertEqual(s.list_to_num(c), a + b)


if __name__ == '__main__':
    unittest.main()
