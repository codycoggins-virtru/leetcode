import unittest
from palindrome import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(121))
        self.assertFalse(s.isPalindrome(-121))
        self.assertFalse(s.isPalindrome(10))
        self.assertFalse(s.isPalindrome(-101))
        self.assertFalse(s.isPalindrome(234524356374568454567645))
        self.assertTrue(s.isPalindrome(76544567))


if __name__ == '__main__':
    unittest.main()
