import unittest
from longest_substring import Solution


class MyTestCase(unittest.TestCase):
    def test_find_unique_string(self):
        s = Solution()
        self.assertEqual(s.find_unique_string("ababab"), "ab")
        self.assertEqual(s.find_unique_string(""), "")
        self.assertEqual(s.find_unique_string("a"), "a")
        self.assertEqual(s.find_unique_string("ab"), "ab")

    def test_lengthOfLongestSubstring(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("ababab"), 2)
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring(""), 0)
        self.assertEqual(s.lengthOfLongestSubstring("abcdddddddddddddddd"), 4)

if __name__ == '__main__':
    unittest.main()
