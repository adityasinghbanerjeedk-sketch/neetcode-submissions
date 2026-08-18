class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap = {}
        for number in nums:
            if number not in countmap:
                countmap[number] = 1
            else:
                countmap[number] += 1
        
        for k in countmap.keys():
            if countmap[k] > 1:
                return True
        
        return False