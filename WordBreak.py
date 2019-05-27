#Given a non-empty string s and a dictionary wordDict containing 
#a list of non-empty words, determine if s can be segmented into 
#a space-separated sequence of one or more dictionary words.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0 or len(s) == 0:
            return False
        check = []
        for i in range(len(s)):
            check.append(False)
        for i in range(len(s)):
            for j in range(0,i+1):
                curr = s[j:i+1]
                if curr in wordDict and (j == 0 or check[j - 1]):
                    check[i] = True
                    break
        return check[len(s) - 1]
