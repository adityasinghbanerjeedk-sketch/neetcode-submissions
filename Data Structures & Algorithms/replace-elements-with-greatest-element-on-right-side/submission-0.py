class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_1 = []
        max_num = 0
        original_len = len(arr)
        for i in range(original_len):
            if len(arr) == 1:
                arr_1.append(-1)
                break
            max_num = arr[1]
            for j in range(1, len(arr)):
                if max_num >= arr[j]:
                    pass
                else:
                    max_num = arr[j]
            arr_1.append(max_num)
            arr.pop(0)
        

        return arr_1