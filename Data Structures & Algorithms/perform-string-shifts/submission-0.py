class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_lst = list(s)
        for lst in shift:
            l_r, cnt = lst[0], lst[1]
            print(l_r, cnt)
            if l_r == 0:
                for i in range(cnt):
                    char = s_lst.pop(0)
                    s_lst.insert(len(s_lst), char)
            else:
                for i in range(cnt):
                    char = s_lst.pop()
                    s_lst.insert(0, char)
        return str("".join(s_lst))