class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        conv_sum = 0
        preceding_value = 0
        for i in range(len(s)):
            num = roman_numerals.get(s[i])
            if i > 0:
              preceding_value = roman_numerals.get(s[i - 1])

            if (num > preceding_value and
                (preceding_value == 1 and (num == 5 or num == 10)) or 
                (preceding_value == 10 and (num == 50 or num == 100)) or 
                (preceding_value == 100 and (num == 500 or num == 1000))):
              # Multiply by 2 to also subtract the preceding iteration from the number given by the combination
              num -= preceding_value * 2
              conv_sum += num
              
            else:
              conv_sum += num
              preceding_value = num
        
        return conv_sum

test = Solution()
print(test.romanToInt("MCMXCIV"))