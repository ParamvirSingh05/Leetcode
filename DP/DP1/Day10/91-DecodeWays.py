class Solution:
    def numDecodings(self, s):
        
        # Recursion => Time Complexity - O(2^n) and Space Complexity - O(n)
        #return self.recursion(s, 0)
    
        # Memoization => Time Complexity - O(n) and Space Complexity - O(n)
        # dp = {}
        # return self.memoization(s, 0, dp)
        
        # DP => Time Complexity - O(n) and Space Complexity - O(n)
        return self.dp(s)
      
    def recursion(self, s, i):
        if i >= len(s):
            return 1
        
        if s[i] == '0':
            return 0
        
        if i == len(s) - 1:
            return 1
        
        res = self.recursion(s, i+1)
        
        if int(s[i:i+2]) <= 26:
            res += self.recursion(s, i+2)
        
        return res
    
    def memoization(self, s, i, dp):
        if i in dp:
            return dp[i]
        
        if i >= len(s):
            return 1
        
        if s[i] == '0':
            return 0
        
        if i == len(s) - 1:
            return 1
        
        res = self.memoization(s, i+1, dp)
        
        if int(s[i:i+2]) <= 26:
            res += self.memoization(s, i+2, dp)
        
        dp[i] = res
        return res
    
    def dp(self, s):
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1
        
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
            
        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            
            last_two_digits = int(s[i-2:i])
            if last_two_digits >= 10 and last_two_digits <= 26:
                dp[i] += dp[i-2]
            
        return dp[len(s)]

s1 = "12"
s2 = "226"
s3 = "06"

res = Solution()

print(res.numDecodings(s1))
print(res.numDecodings(s2))
print(res.numDecodings(s3))