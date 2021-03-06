#You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed. All houses at this
#place are arranged in a circle. That means the first house is the neighbor
#of the last one. Meanwhile, adjacent houses have security system connected 
#and it will automatically contact the police if two adjacent houses were 
#broken into on the same night.Given a list of non-negative integers representing 
#the amount of money of each house, determine the maximum amount of money 
#you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3: 
            return max(nums) 
        first = nums[0]
        second = nums[1]
        third = nums[2]
        fourth = nums[0] + nums[2]
        for n in range(3, len(nums)):
            second, first, third, fourth = max(second, third), max(first, fourth), second+nums[n], first+nums[n]
        return max(second, first, third)
