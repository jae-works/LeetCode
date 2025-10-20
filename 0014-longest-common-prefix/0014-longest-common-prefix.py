class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_list = []
        for idx, char in enumerate(strs[0]):
            for strs_idx in range(1, len(strs)):
                if len(strs[strs_idx]) - 1 < idx:
                    return "".join(result_list)
                if strs[strs_idx][idx] != char:
                    return "".join(result_list)
            result_list.append(char)
        return "".join(result_list)
                
            