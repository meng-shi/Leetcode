class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors) + k
        num_alt_colors = [-1] * n
        count = 0
        for i in range(n):
            if i == 0:
                num_alt_colors[i] = 1
            if colors[i % len(colors)] != colors[(i-1) % len(colors)]:
                num_alt_colors[i] = num_alt_colors[i-1] + 1
            else:
                num_alt_colors[i] = 1
        for i in range(k, n):
            if num_alt_colors[i] >= k:
                count +=1
        return count
