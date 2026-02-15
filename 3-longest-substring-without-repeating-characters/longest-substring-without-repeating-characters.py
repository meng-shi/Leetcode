class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        sub = set()
        count = 0
        for r in range (n):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            count = max(count, r-l+1)
        return count