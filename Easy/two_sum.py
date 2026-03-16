from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        arr = []
        index = 0
        for curr in nums:
            if (target - curr) in num_dict:
                arr.append(num_dict[target - curr])
                arr.append(index)
                break
            num_dict[curr] = index
            index += 1
        return arr
    
test = Solution()
nums = [20, 30, 12, 38, 21, 40]
target = 33
print(test.twoSum(nums, target))