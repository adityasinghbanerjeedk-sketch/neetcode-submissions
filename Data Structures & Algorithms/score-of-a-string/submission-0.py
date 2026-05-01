class Solution:
    def scoreOfString(self, s: str) -> int:
        leng = len(s)
        lst = list(s)
        sum_abs = 0
        for i in range(len(lst)):
            if leng == 1:
                break  
            sum_abs = sum_abs + abs(ord(lst[i]) - ord(lst[i + 1]))
            leng -= 1
        return sum_abs