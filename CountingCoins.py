#You are given coins of different denominations and a total amount
#of money amount. Write a function to compute the fewest number of
#coins that you need to make up that amount. If that amount of money 
#cannot be made up by any combination of the coins, return -1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ret = [amount+1] * (amount+1)
        ret[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    ret[i] = min(ret[i], ret[i-c] + 1)

        if ret[amount] == amount+1:
            return -1
        return ret[amount]        
