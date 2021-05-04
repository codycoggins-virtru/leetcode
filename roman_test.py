import unittest
from roman import Solution


class MyTestCase(unittest.TestCase):
    def test_mapping(self):
        s = Solution()

        self.assertEqual(s.rome['I'], 1)

    def test_simple_conversions(self):
        s = Solution()
        self.assertEqual(3, s.romanToInt("III"))
        self.assertEqual(58, s.romanToInt("LVIII"))

    def test_minus_conversions(self):
        s = Solution()
        self.assertEqual(4, s.romanToInt("IV"))
        self.assertEqual(9, s.romanToInt("IX"))

    # def test_double_minus_conversions(self):
    #     s = Solution()
    #     self.assertEqual(1994,s.romanToInt("MCMXCIV"))


if __name__ == '__main__':
    unittest.main()
