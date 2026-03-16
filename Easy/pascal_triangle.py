from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr_2d = [[1]]
        if numRows >= 2:
            arr_2d.append([1, 1])
        for n in range(2, numRows):
            arr_2d.append([])
            for k in range(n+1):
                if k == 0  or k == n:
                    arr_2d[n].append(1)
                else:
                    arr_2d[n].append(arr_2d[n-1][k-1] + arr_2d[n-1][k])
                    
        return arr_2d
    

generate_instance = Solution()
print(generate_instance.generate(5))