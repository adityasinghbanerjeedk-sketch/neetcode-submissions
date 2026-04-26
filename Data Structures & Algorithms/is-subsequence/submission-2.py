class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        current_t = list(t)
        for char_s in s:
            while len(current_t) > 0:
                char_t = current_t.pop(0)
                if char_s == char_t:
                    c += 1
                    break
        if c == len(s):
            return True
        else:
            return False