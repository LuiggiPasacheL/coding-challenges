
class Solution:

    # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    # An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # open bracket must be closed in the same order
    # Every close bracket has a corresponding open bracket of the same type
    # Examples:
    # s = "()" Output: true
    # s = "()[]{}" Output: true
    # s = "(]" Output: false
    # s = "([])" Output: true
    # s = "([]})" Output: false


    def isValid(self, s: str) -> bool:

        memory = []

        close_open_brackets = { 
            "}": "{", 
            ")": "(", 
            "]": "[" 
        }

        for c in s:
            if c not in close_open_brackets: # is open bracket
                memory.append(c)
            else: # is close bracket
                if len(memory) == 0:
                    return False

                aux = memory.pop()

                if aux != close_open_brackets[c]:
                    return False
        
        return len(memory) == 0
