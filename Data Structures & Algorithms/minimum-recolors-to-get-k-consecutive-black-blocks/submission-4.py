class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        hashmap = {}

        L = 0
        res = float("inf")
        for R in range(len(blocks)):
            hashmap[blocks[R]] = 1 + hashmap.get(blocks[R], 0)

            if (R - L + 1) > k:
                hashmap[blocks[L]] -= 1
                L += 1
                res = min(res, hashmap['W'])
        if 'W' in hashmap:
            res = min(res, hashmap['W'])
                
            
            
            

        print(hashmap)
        print(res) 
        return res if 'W' in hashmap else 0