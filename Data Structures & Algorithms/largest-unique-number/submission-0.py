class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        # print(max(hashmap))
        for i in range(len(hashmap)):
            k = max(hashmap)
            # print(k)
            if hashmap[k] == 1:
                return k
            else:
                del hashmap[k]
        return -1
            