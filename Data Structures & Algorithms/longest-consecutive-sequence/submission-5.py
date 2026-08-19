class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = list(sorted(set(nums)))
        print(new_list)
        if len(new_list) < 1:
            return 0
        elif len(new_list) == 1:
            return 1
        max_seq = 1
        c = 1
        for index, num in enumerate(new_list[:-1]):
            next_num = new_list[index+1]
            if next_num - num == 1:
                c += 1
                max_cons = c
                if max_seq < max_cons:
                    max_seq = max_cons
            else:
                c = 1
        return max_seq
        