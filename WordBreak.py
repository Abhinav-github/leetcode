#Given a non-empty string s and a dictionary wordDict containing 
#a list of non-empty words, determine if s can be segmented into 
#a space-separated sequence of one or more dictionary words.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0 or len(s) == 0:
            return False
        
        check = []
        for i in range(len(wordDict)):
            check.append(False)
            
        check[0] = True
        for i in range(len(wordDict)):
            for j in range(0,i):
                curr = s[j:i+1]
                if curr in wordDict and (j == 0 or check[j - 1]):
                    check[i] = True
                    break
        return check[len(wordDict) - 1]
