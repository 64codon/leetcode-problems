class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if x < 0:
           return False
        else:
          while temp != 0:
            rev = (rev * 10) + (temp % 10)
            temp = temp // 10
          return rev == x

test = Solution()
print(test.isPalindrome(-121))