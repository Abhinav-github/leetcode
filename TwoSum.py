#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        answer = []
        for i in range(len(nums)):
            if nums[i] in hash:
                answer.append(hash[nums[i]])
                answer.append(i)
                return answer
            hash[target - nums[i]] = i
        return answer
