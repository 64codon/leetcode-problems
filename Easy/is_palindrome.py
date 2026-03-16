class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp_x1 = x
        temp_x2 = x
        reversed_x = 0
        num_digits = 0

        while temp_x1 > 0:
            num_digits +=1
            temp_x1 = temp_x1 // 10

        while num_digits > 0:
            reversed_x += (temp_x2 % 10) * 10**(num_digits-1)
            temp_x2 = temp_x2 // 10
            num_digits -= 1
        
        return x == reversed_x

        
print(Solution().isPalindrome(121))