class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        L, R = 0, 0
        num_zero = 0

        while R < len(nums):
            if nums[R] == 0:
                num_zero += 1

            while num_zero == 2:
                if nums[L] == 0:
                    num_zero -= 1
                L += 1

            longest = max(longest, R - L + 1)
            R += 1
        return longest