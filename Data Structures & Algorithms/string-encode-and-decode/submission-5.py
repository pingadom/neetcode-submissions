class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)).zfill(3))
            res.append(s)
        return "".join(res)
            
        

    def decode(self, s: str) -> List[str]:
        p1 = p2 = 0
        res = []
        if s == []:
            return []
        
        while p2 < len(s):
            num = int(s[p2:p2+3])
            p1 = p2 + 3
            p2 += 3 + num
            res.append(s[p1:p2])
            
        return res


