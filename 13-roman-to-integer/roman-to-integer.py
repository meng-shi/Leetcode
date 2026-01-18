class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        n = len(s)
        i = 0
        
        while i < n:
            if i < n - 1 and dic[s[i]]  < dic[s[i+1]]:
                sum += dic[s[i+1]] - dic[s[i]]
                i +=2
            else:
                sum += dic[s[i]]
                i += 1
        return sum
          