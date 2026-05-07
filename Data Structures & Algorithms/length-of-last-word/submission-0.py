class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        lst = list(s)
        cnt = 0
        for char in reversed(lst):
            if char != " ":
                cnt += 1
            else:
                break
        return cnt