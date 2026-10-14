class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = list(s1)
        k = len(s1_list)
        lst = []
        for r in range(len(s2)):
            c = s2[r]

            lst.append(c)

            while len(lst) == k:
                if sorted(lst) == sorted(s1_list):
                    return True
                lst.pop(0)
        return False

                

            

            

                

            
                    