from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        i = 0
        done: bool = False
        while not done:
            if i >= len(strs[0]):
                break
            char: str = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    done = True
                    break
            if not done:
                i += 1
        return strs[0][0:i]


solution = Solution()
testcases = [
    ["flower", "flow", "flight"],
    ["dog","racecar","car"],
    [],
    ["spamspam"]
]
for t in testcases:
    print(f'{t}: {solution.longestCommonPrefix(t)}')
