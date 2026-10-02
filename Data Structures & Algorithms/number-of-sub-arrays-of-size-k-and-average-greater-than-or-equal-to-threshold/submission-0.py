class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = list()
        L = 0
        c= 0
        for R in range(len(arr) + 1):
            if R - L >= k:
                if sum(window) / k >= threshold:
                    c += 1
                window.pop(0)
                L += 1
            if R < len(arr):
                window.append(arr[R])
            else:
                return c
