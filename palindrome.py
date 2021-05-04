class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = list(str(x))
        reverse = forward[::-1]
        return forward == reverse
