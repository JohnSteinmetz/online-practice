class Solution:
    def searchInsert(self, nums, target) -> int:
        for index, value in enumerate(nums):
            if (target < value or target == value):
                return index
      
        return len(nums)