class Solution:
    def wordBreak(self, s, wordDict):
        start_index = 0
        end_index = 1
        dp = {}
        i = 0
        #res = self.recursion(wordDict, s, start_index, end_index)
        res = self.recursion1(wordDict, s, i)
        return res
    
    def recursion(self, wordDict, s, start_index, end_index):
        if s[start_index:end_index] == "":
            return True
        
        if end_index > len(s):
            return False
        
        if s[start_index:end_index] in wordDict:
            return self.recursion(wordDict, s, end_index, end_index+1) or self.recursion(wordDict, s, start_index, end_index+1)
        else:
            return self.recursion(wordDict, s, start_index, end_index+1)

    def recursion1(self, wordDict, s, i):
        if i == len(s):
            return True
        
        res = False
        for word in wordDict:
            temp = False
            if s[i:len(word)+i] in wordDict:
                temp = self.recursion1(wordDict, s, len(word)+i)
            res = res or temp
        
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