class Solution:
    def isValid(self, s: str) -> bool:
        openpairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        closepairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in openpairs.keys():
                stack.append(char)
            else:
                if not stack:
                    return False # happens when theres a closing bracket without an opening one
                if stack[-1] != closepairs.get(char):
                    return False
                stack.pop()
        return True if not stack else False
                
        