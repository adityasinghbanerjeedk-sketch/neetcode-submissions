class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        hashset = set()
        L , res = 0, 0

        for R in range(len(s)):

            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1

            hashset.add(s[R])
            if R - L + 1 > k:
                hashset.remove(s[L])
                L += 1
            if R - L + 1 == k:
                res += 1
        return res