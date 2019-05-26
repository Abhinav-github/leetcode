#Given an unsorted array of integers, find the length of longest increasing subsequence.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_sub = []
        for i in range(len(nums)):
            longest_sub.append(1)
            
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if longest_sub[j] + 1 > longest_sub[i]:
                        longest_sub[i] = longest_sub[j] + 1
        
        return max(longest_sub)
