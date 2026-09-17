class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) -1
        l = 0
        # remove the ending spaces
        while s[n] == ' ':
                n -= 1
        
        while n >= 0:
            if s[n] == ' ':
                return l
            l += 1
            n -= 1
        
        return l
            
            
        
        