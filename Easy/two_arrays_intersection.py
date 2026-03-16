from typing import List

# TODO: Optimize with binary search
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(arr, targetValue):
            lowIndex = 0
            highIndex = len(arr) - 1

            while highIndex >= lowIndex:
                middleIndex = (lowIndex+highIndex) // 2

                if arr[middleIndex] < targetValue:
                    lowIndex = middleIndex + 1

                elif arr[middleIndex] > targetValue:
                    highIndex = middleIndex - 1
                
                else:
                    return arr[middleIndex]
                
            return

        # nums2 is always the bigger list        
        if len(nums2) < len(nums1):
            # I apparently could do this with tuple unpacking, but I am more used to working with temp variables. Maybe next time!
            temp = nums2
            nums2 = nums1
            nums1 = temp

        # Sort the bigger list which is going to be used to call the binary_search function
        nums2.sort()

        intersection_arr = []
        for target in nums1:
            result = binary_search(nums2, target)
            if result is not None and result not in intersection_arr:
                intersection_arr.append(result)

        return intersection_arr

test = Solution()
print(test.intersection([9,4,9,8,4], [4,9,5]))