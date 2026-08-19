class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap and hashmap[complement] != index:
                return [index, hashmap[complement]]