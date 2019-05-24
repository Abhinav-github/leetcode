#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            c = a + b 
            a = b
            b = c
        return a
