
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest: str = s[0]

        # odd length answers
        for i in range(0, len(s)):
            j: int = 1
            best_j: int = 0
            while (i-j) >= 0 and (i+j) < len(s) and s[i-j] == s[i+j]:
                if (2 * j + 1) > len(longest):
                    best_j = j
                j += 1
            if best_j:
                longest = s[i-best_j:i+best_j+1]

        # even length answers
        for i in range(0, len(s)):
            j: int = 1
            best_j: int = 0
            while (i-j) >= 0 and (i+j-1) < len(s) and s[i-j] == s[i+j-1]:
                if (2 * j) > len(longest):
                    best_j = j
                j += 1
            if best_j:
                longest = s[i-best_j:i+best_j]

        return longest


solution = Solution()
testcases = [
    "abcba",
    "zabcbaa",
    "cbbd",
    "a",
    "ac",
    ""
]
for t in testcases:
    print(f'{t}: {solution.longestPalindrome(t)}')
