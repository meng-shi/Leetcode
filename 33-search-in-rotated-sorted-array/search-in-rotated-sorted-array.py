class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = low + (high-low)//2
            #print(high, nums[mid])
            if target == nums[mid]:
                return mid
            if (nums[low] <= nums[mid]):
                print(nums[low],nums[mid])
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid+1
            
            else:
                if nums[mid] < target <= nums[high-1]:
                    low = mid+1
                else:
                    high = mid

        return -1

                
                
