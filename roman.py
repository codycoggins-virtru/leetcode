class Solution:
    rome = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

    def romanToInt(self, s: str) -> int:
        chars = list(s)
        total = 0
        for i in range(0, len(chars)):
            val = self.rome[chars[i]] 
            if i == len(chars)-1:
                # Last char
                total += val
            elif val < self.rome[chars[i+1]]:
                # Minus
                total -= val
            else:
                # Normal
                total += val
        return total

    def naive(self, s: str) -> int:
        chars = list(s)
        naive = [self.rome[c] for c in chars]
        return sum(naive)
