from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(left_pointer, right_pointer):
            middle_pointer = (right_pointer + left_pointer) // 2

            if right_pointer >= left_pointer: # Greater than or equal to ensure that the points never cross over and that the function doesn't ignore the last element in the array when both pointers are on the same element.
                
                if target < nums[middle_pointer]:
                    return helper(left_pointer, middle_pointer - 1) # Minus one to move one step toward the left

                elif target > nums[middle_pointer]:
                    return helper(middle_pointer + 1, right_pointer) # Plus one to move one step toward the right
                
                elif target == nums[middle_pointer]:
                    return middle_pointer
                
            else: 
                return -1 # If the condition right_pointer >= left_pointer was exhausted, return -1 and exit the function. The list has been fully iterated over.
                
        return helper(0, len(nums) - 1)

nums = [-1,0,3,5,9,12]

func = Solution()
print(func.search(nums, 9))