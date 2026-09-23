class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        res = []

        for ch in order:
            if ch in count:
                res.append(ch * count[ch])
                del count[ch]
            
        
        for c, freq in count.items():
            res.append(c * freq)
        
        return "".join(res)