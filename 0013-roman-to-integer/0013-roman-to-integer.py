class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        numerals_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        out_num = numerals_dict.get(s[-1])
        for idx in range(1, len(s)):
            if numerals_dict.get(s[-idx-1]) < numerals_dict.get(s[-idx]):
                out_num -= numerals_dict.get(s[-idx-1])
            else:
                out_num += numerals_dict.get(s[-idx-1])
        return out_num
