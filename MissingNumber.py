#Given an array containing n distinct numbers taken from 
#0, 1, 2, ..., n, find the one that is missing from the array.

#slow version
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

#assuming missing value replaced with next value
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        expected_sum = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            expected_sum += i
        sum1 -= len(nums)
        return expected_sum - sum1
