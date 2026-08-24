class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        prefix[0] = 1
        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i-1]
        

        suffix = [1] * length
        suffix[length - 1] = 1
        for i in range(length-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        prod = [1] * length
        for i in range(0, length):
            prod[i] = prefix[i] * suffix[i]
        return prod