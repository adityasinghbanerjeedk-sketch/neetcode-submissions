class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i,n in enumerate(numbers):
            hashmap[n] = i

        for i, n in enumerate(numbers):
            complement = target - n

            if complement in hashmap and hashmap[complement] != i:
                return [i+1, hashmap[complement] + 1]
