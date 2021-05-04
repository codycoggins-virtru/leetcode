class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        length = len(longest)
        for i in range(0, len(s)):
            if len(s[i:]) <= length:
                break
            unique: str = self.find_unique_string(s[i:])
            print(f'unique = {unique}')
            if unique and len(unique) > length:
                print("new winner")
                longest = unique
                length = len(unique)
        return length

    @staticmethod
    def find_unique_string(s: str) -> str:
        print(f'check {s}')
        if not s:
            return ""
        found: set = set([])
        if len(s) == 1:
            return s
        for i in range(0, len(s)):
            if s[i] in found:
                return s[:i]
            found.add(s[i])
        return s
