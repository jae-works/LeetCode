class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_str = ""
        for idx, char in enumerate(strs[0]):
            for strs_idx in range(1, len(strs)):
                if len(strs[strs_idx]) - 1 < idx:
                    return result_str
                if strs[strs_idx][idx] != char:
                    return result_str
            result_str += char
        return result_str
                
            