class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        L = 0
        R = k - 1
        res = float('inf')
        print(nums)
        while R < len(nums):
            print(nums[R], nums[L])
            res = min(res, nums[R] - nums[L])
            R += 1
            L += 1
            print(res)
        return res