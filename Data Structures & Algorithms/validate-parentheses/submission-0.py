class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # for closing
            if char in mapping:
                top_element= stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            
            else:
                # for opening
                stack.append(char)
        
        return not stack
        