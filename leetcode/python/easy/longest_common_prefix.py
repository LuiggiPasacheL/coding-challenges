from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for word in strs:
            for i in range(len(prefix)):
                if i >= len(word) or prefix[i] != word[i]:
                    prefix = prefix[:i]
                    break

        return prefix

    def longestCommonPrefixV2(self, strs: List[str]) -> str:
        first_word = strs[0]

        prefix = ""

        for i in range(len(first_word)):
            append = True
            for word in strs:
                if i >= len(word) or word[i] != first_word[i]:
                    append = False
            if append:
                prefix += first_word[i]
            else:
                break

        return prefix

