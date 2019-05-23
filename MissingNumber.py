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
    
class Solution:
def missingNumber(self, nums: List[int]) -> int:
