#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#Find the minimum element.
#You may assume no duplicate exists in the array.

#naive method
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < nums[0]:
                return nums[i]
        return nums[0]
    
    def findMinNew(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        left = 0
        right = (len(nums) - 1)
        middle = (left + right)//2
        while left < right:
            if nums[middle] > nums[middle + 1]:
                return nums[middle+1]
            elif nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
            middle = (left + right)//2
        return nums[0]
        
