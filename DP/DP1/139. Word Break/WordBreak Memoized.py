class Solution:
    def wordBreak(self, s, wordDict):
        start_index = 0
        end_index = 1
        dp = {}
        i = 0
        #res = self.recursion(wordDict, s, start_index, end_index, dp)
        res = self.recursion1(wordDict, s, i, dp)
        return res
    
    def recursion(self, wordDict, s, start_index, end_index, dp):
        if s[start_index:end_index] == "":
            return True
        
        if end_index > len(s):
            return False
        
        if start_index in dp:
            return dp[start_index]
        
        if s[start_index:end_index] in wordDict:
            dp[start_index] = self.recursion(wordDict, s, end_index, end_index+1, dp) or self.recursion(wordDict, s, start_index, end_index+1, dp)
            return dp[start_index]
        else:
            dp[start_index] = self.recursion(wordDict, s, start_index, end_index+1, dp)
            return dp[start_index]
        
    
    def recursion1(self, wordDict, s, i, dp):
        if i == len(s):
            return True
        
        if i in dp:
            return dp[i]
        
        res = False
        for word in wordDict:
            temp = False
            if s[i:len(word)+i] in wordDict:
                temp = self.recursion1(wordDict, s, len(word)+i, dp)
            res = res or temp
        
        dp[i] = res
        
        return res


res = Solution()

s1 = "leetcode"
wordDict1 = ["leet","code"]
print(res.wordBreak(s1, wordDict1))

s2 = "applepenapple"
wordDict2 = ["apple","pen"]
print(res.wordBreak(s2, wordDict2))

s3 = "catsandog"
wordDict3 = ["cats","dog","sand","and","cat"]
print(res.wordBreak(s3, wordDict3))