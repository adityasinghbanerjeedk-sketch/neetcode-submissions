class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max_cons = 0
        for i in nums:
            if i == 1:
                c += 1
                if max_cons < c:
                    max_cons = c
            else:
                c = 0
        return max_cons        
        