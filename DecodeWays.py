#A message containing letters from A-Z is being encoded to numbers using the following mapping:

#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number of ways to decode it.

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ret = [1] + [0] * len(s)
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                ret[i] += ret[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26: 
                ret[i] += ret[i-2]
        return ret[len(s)]
