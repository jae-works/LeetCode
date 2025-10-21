class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or len(needle) == 1 and needle[0] == haystack[0]:
            return 0

        for haystack_idx in range(len(haystack) - len(needle) + 1):
            if haystack[haystack_idx] == needle[0]:
                if len(needle) == 1:
                    return haystack_idx
                for needle_idx in range(1, len(needle)):
                    if haystack[haystack_idx+needle_idx] == needle[needle_idx]:
                        if needle_idx == len(needle) - 1:
                            return haystack_idx
                    else:
                        break
                        
        return -1
