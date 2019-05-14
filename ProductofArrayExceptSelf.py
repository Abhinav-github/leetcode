#Given an array nums of n integers where n > 1,  
#return an array output such that output[i] is 
#equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        length = len(nums)
        right_total = 1
        for i in range(len(nums)):
            answer.append(right_total)
            right_total = right_total * nums[i]
        left_total = 1
        for i in range(len(nums) - 1, -1,-1):
            answer[i] = left_total * answer[i]
            left_total = left_total * nums[i]
        return answer
