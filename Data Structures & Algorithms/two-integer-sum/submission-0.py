class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for k, v in enumerate(nums):
            hashmap[v] = k
        for k, v in enumerate(nums):
            # print(v)
            complement = target - v
            if complement in hashmap and hashmap[complement] != k:
                return [k,hashmap[complement]]