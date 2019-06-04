#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach 
#the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        one = math.factorial(m + n - 2)
        two = math.factorial(m-1)
        three = math.factorial(n-1)
        return int(one/two/three)
