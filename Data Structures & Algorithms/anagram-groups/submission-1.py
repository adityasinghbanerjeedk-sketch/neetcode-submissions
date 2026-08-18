class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            anagram = "".join(sorted(word))
            if anagram not in hashmap:
                hashmap[anagram] = [word]
            else:
                hashmap[anagram].append(word)
        return list(hashmap.values())
