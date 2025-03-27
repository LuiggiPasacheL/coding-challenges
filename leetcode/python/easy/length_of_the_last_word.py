class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        reversal_word = ""

        for l in s[::-1]:

            if l == " " and reversal_word != "":
                break
            elif l == " ":
                continue
            
            reversal_word += l


        return len(reversal_word)


Solution().lengthOfLastWord("Hello World")
