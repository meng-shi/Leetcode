class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            left = target-nums[i]
            if left in result:
                return [result[left],i]
            result[nums[i]]= i

        return []



