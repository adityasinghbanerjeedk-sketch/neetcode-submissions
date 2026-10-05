class Solution:
    def confusingNumber(self, n: int) -> bool:
        hashmap = {
            '0' : 0,
            '1' : 1,
            '6' : 9,
            '8' : 8,
            '9' : 6

        }
        lst = []
        rotated_str = ""

        for i in reversed(str(n)):
            if i in hashmap:
                lst.append(str(hashmap[i]))
            else:
                return False

        rotated_str = "".join(lst) 
        print(rotated_str)       

        return True if int(rotated_str) != n else False      