class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        min_val = min(arrays[0])
        max_val = max(arrays[0])
        cur_min, cur_max, res = 0, 0, 0
        arrays.pop(0)
        for arr in arrays:
           cur_min, cur_max = min(arr), max(arr)
           res = max(res, max(abs(cur_min - max_val), abs(cur_max - min_val)))

           min_val = min(cur_min, min_val)
           max_val = max(cur_max, max_val)

        return res