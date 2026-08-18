class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 , hash_2 = {}, {}
        for char in s:
            if char not in hash_1:
                hash_1[char] = 1
            else:
                hash_1[char] += 1
        
        for char in t:
            if char not in hash_2:
                hash_2[char] = 1
            else:
                hash_2[char] += 1


        if hash_1 == hash_2:
            return True
        else:
            return False
        