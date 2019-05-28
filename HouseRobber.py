class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        money = []
        for i in range(len(nums)):
            money.append(0)
        for i in range(len(nums)):
            if i == 0 or i == 1:
                money[i] = nums[i]
            else:
                money[i] = nums[i] + max(money[0:i-2])
        return max(money)
