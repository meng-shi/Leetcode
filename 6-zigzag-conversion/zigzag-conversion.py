class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        i = 0
        d = 1

        for char in s :
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
    
        return ''.join(rows)
