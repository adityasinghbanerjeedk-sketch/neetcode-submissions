class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap_1, hashmap_2 = {}, {}
        lst = []
        for idx, val in enumerate(nums1):
            hashmap_1[val] = idx
        for idx, val in enumerate(nums2):
            hashmap_2[val] = idx
        print(hashmap_1)
        print(hashmap_2)
        for i in nums1:
            if i in hashmap_2:
                # print(hashmap_2[i])
                lst.append(hashmap_2[i])
        
        # print(lst)
        return lst
        # hashmap_1, hashmap_2 = defaultdict(list), defaultdict(list)
        # for idx, val in enumerate(nums1):
        #     hashmap_1[val].append(idx)
        # for idx, val in enumerate(nums2):
        #     hashmap_2[val].append(idx)

        # print(hashmap_1)