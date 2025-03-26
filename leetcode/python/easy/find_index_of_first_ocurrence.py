
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_len = len(needle)
        for i in range(len(haystack) - needle_len):
            
            maybe_needle = haystack[i:i+needle_len]

            if (maybe_needle == needle):
                return i

        return -1


Solution().strStr("mississippi", "issip")
