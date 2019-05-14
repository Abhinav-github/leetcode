#Given an integer array nums, find the contiguous subarray 
#(containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        result = nums[0]
        for i in range(len(nums)):
            current += nums[i]
            result = max(current,result)
            current = max(0,current)
        return result
