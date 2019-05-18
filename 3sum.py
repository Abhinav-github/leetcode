#Given an array nums of n integers, are there elements a, b, c 
#in nums such that a + b + c = 0? Find all unique triplets in 
#the array which gives the sum of zero.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ret.append((nums[i], nums[left],nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1
                        
                    left += 1
                    right -= 1
        return list(set(tuple(ret)))
