class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        for R in range(1, len(nums)):
            if nums[R] == nums[L]:
                nums[L] = 'r'
            L += 1
        print(nums)
        while 'r' in nums:
            nums.remove('r')
        print(nums)    
        return len(nums)
            

        