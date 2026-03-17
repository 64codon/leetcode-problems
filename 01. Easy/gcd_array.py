from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)

        while a != b:
            if a < b:
                b -= a
            else:
                a -= b
        return a
    
nums = [10,6,9]
func = Solution()

print(func.findGCD(nums))
          