class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')     
        n = len(nums)
        summ = 0
        l = 0

        for r in range(n):
            summ += nums[r]
            while summ >= target:
                length = min(length, r-l+1)
                summ -= nums[l]
                l += 1
            
        if length == float('inf'):
            return 0
        else:
            return length

        

