#Given an integer array with all positive numbers and no 
#duplicates, find the number of possible combinations that
#add up to a positive integer target

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target == 0:
            return 0
        tar = []
        for i in range(target +  1):
            tar.append(0)
        for i in range(1, target+1):
            for j in nums:
                if i == j:
                    tar[i] += 1
                elif i - j > 0:
                    tar[i] += tar[i - j]
        return tar[target]
