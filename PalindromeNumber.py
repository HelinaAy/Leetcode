class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Negative numbers are not palindromes
            return False

        reversed_num = 0
        original_num = x
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10  # Reduce x

        return reversed_num == original_num
