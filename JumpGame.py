#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= final:
                final = i
        return not final
