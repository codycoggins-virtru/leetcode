from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        action: dict = {'(': ')',
                        '[': ']',
                        '{': '}'}
        i: int = 0
        stack: List = []
        while i < len(s):
            if s[i] in action:
                stack.append(action[s[i]])
            elif stack and s[i] == stack[-1]:
                stack.pop()
            else:
                return False
            i += 1

        return not stack




sol = Solution()
testcases = [
    "()",
    "()[]{}",
    "",
    "(]",
    "([)]"
]

for t in testcases:
    print(f'{t}: {sol.isValid(t)}')
