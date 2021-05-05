import sys


class Solution:
    def reverse(self, x: int) -> int:

        """
        :type x: int
        :rtype: int
        """

        digits = list(str(x))
        if digits[0] == "-":
            # Handle negative numbers
            del digits[0]
            digits.reverse()
            digits.insert(0, "-")
        else:
            digits.reverse()

        reversed = ""
        for d in digits:
            reversed += d

        r = int(reversed)
        if r > (2 ** 31 - 1):
            return 0
        if r < (-2 ** 31):
            return 0
        return r
