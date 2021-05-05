class Solution:
    max = 2 ** 31 - 1
    min = -2 ** 31

    def myAtoi(self, s: str) -> int:
        digits = list(s.strip())

        if len(digits) == 0:
            return 0
        if digits[0] == "+":
            if len(digits) == 1 or not digits[1].isdigit():
                return 0
            else:
                return self.toint(digits[1:])
        return self.toint(digits)

    def toint(self, d: list) -> int:
        parsed = self.parse(d)
        if parsed == "":
            return 0
        try:
            r = int(parsed)
        except:
            return 0
        if r > (self.max):
            return self.max
        if r < (self.min):
            return self.min
        return r

    def parse(self, d: list) -> str:
        if d[0].isdigit() or d[0] == "-":
            if len(d) == 1 or not d[1].isdigit():
                # terminating case
                return d[0]
            else:
                return d[0] + self.parse(d[1:])

        return ""