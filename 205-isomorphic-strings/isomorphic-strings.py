class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        n = len(s)
        if len(t) != n:
            return False
        for i in range(n):
            s1 = s[i]
            t1 = t[i]

            if ((s1 in map_s and map_s[s1] != t1) or (t1 in map_t and map_t[t1] != s1)):
                return False
            
            map_s[s1] = t1
            map_t[t1] = s1
        return True
