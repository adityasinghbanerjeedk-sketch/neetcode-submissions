class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        # print(hashmap.items())
        arr = []
        for num, cnt in hashmap.items():
            arr.append([cnt, num])
        print(arr)
        arr.sort()
        print(arr)
        res = []
        while len(res)< k:
            res.append(arr.pop()[1])
        return res