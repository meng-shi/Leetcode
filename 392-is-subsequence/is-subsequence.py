class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        index_t = 0
        while index_t < len(t) and index_s < len(s):
            if s[index_s] == t[index_t]:
                index_s +=1
            index_t +=1
        return index_s == len(s)

            

