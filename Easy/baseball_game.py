from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec_arr = []
        for element in operations:
          if element == 'C':
              rec_arr.pop()
          elif element == 'D':
              double_latest = rec_arr[-1] * 2
              rec_arr.append(double_latest)
          elif element == '+':
              previous_sum = rec_arr[-1] + rec_arr[-2]
              rec_arr.append(previous_sum)
          else:
              rec_arr.append(int(element))
        return sum(rec_arr)
                
            


game = Solution()
print(game.calPoints(["5","-2","4","C","D","9","+","+"]))