from typing import List

class Solution:
    
    def getRow(self, rowIndex: int) -> List[int]:
      def fac(n):
        if n == 0:
            return 1
        fac = 1
        for i in range (n, 0, -1):
            fac *= i
        return fac
      
      row = []
      fac_num = fac(rowIndex)
      for k in range(rowIndex + 1):
         fac_den = (fac(k)*fac(rowIndex-k))
         col = fac_num // fac_den
         row.append(col)
      return row

        
print(Solution().getRow(3))     
                