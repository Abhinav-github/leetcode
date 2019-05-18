#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#You may assume no duplicate exists in the array.
#Your algorithm's runtime complexity must be in the order of O(log n).

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            current = (left + right) // 2
            
            if target == nums[current]:
                return current
            
            if nums[left] <= nums[current]:
                if nums[left] <= target and target <= nums[current]:
                    right = current - 1
                else:
                    left = current + 1

                    
            else:
                if nums[current] <= target and target <= nums[right]:
                    left = current + 1
                else:
                    right = current - 1
        
        return -1
