class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = c = 0

        for R in range(1, len(nums)):
            if nums[L] == nums[R] and c < 1:
                c += 1
            elif nums[L] == nums[R] and c > 0:
                nums[R] = '_'
            elif nums[L] != nums[R]:
                L = R
                c = 0
        L = 0
        for R in range(len(nums)):
            if nums[R] != '_':
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        return L
        