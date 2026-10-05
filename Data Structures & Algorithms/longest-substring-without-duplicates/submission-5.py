class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        L, res = 0, 0

        for R in range(len(s)):

            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1
            hashset.add(s[R])
            res = max(res, R - L + 1)

        return res if len(s) > 0 else 0