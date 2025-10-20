class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        if x < 10:
            return True

        tmp = x
        x_len = 0
        while tmp > 0:
            tmp = tmp // 10
            x_len += 1

        for num in range(x_len // 2):
            if (x // (10 ** (x_len - num - 1))) % 10 != x // (10 ** (num)) % 10:
                return False
        return True

        

        