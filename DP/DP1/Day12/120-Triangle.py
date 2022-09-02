class Solution:
    def minimumTotal(self, triangle):
        # Recursion => Time Complexity - O(2^n) and Space Complexity - O(n) - Gives TLE
        # min_sum = self.recursive(triangle, 0, 0)
        # return min_sum
        
        # Memoization => Time Complexity - O(n^2) and Space Complexity - O(n^2)
        # dp = [[None for _ in range(len(triangle))] for _ in range(len(triangle))]
        # return self.memoization(triangle, 0, 0, dp)
        
        # Tabulation => Time Complexity - O(n^2) and Space Complexity - O(n^2)
        # return self.tabulation(triangle)
        
        # tabulation space optimized => Time Complexity - O(n^2) and Space Somplexity - O(1)
        return self.space_optimization(triangle)
    
    def recursive(self, triangle, row, column):
        if row == len(triangle) - 1:
            return triangle[row][column]
        
        min_path = triangle[row][column] + min(self.recursive(triangle, row+1, column),
                                              self.recursive(triangle, row+1, column+1))
        
        return min_path
    
    def memoization(self, triangle, row, column, dp):
        if row == len(triangle) - 1:
            return triangle[row][column]
        
        if dp[row][column] != None:
            return dp[row][column]
        
        min_path = triangle[row][column] + min(self.memoization(triangle, row+1, column, dp),
                                              self.memoization(triangle, row+1, column+1, dp))
        
        dp[row][column] = min_path
        
        return min_path
    
    def tabulation(self, triangle):
        dp = [[None for _ in range(len(triangle))] for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        
        for row in range(1, len(triangle)):
            for column in range(row+1):
                if column == 0:
                    dp[row][column] = triangle[row][column] + dp[row-1][column]
                elif column == row:
                    dp[row][column] = triangle[row][column] + dp[row-1][column-1]
                else:
                    dp[row][column] = triangle[row][column] + min(dp[row-1][column], dp[row-1][column-1])
        
        last_row = len(triangle) - 1
        min_path = float('inf')
        for column in range(len(triangle)):
            min_path = min(min_path, dp[last_row][column])
        return min_path
    
    def space_optimization(self, triangle):
        for row in range(1, len(triangle)):
            for column in range(row+1):
                if column == 0:
                    triangle[row][column] = triangle[row][column] + triangle[row-1][column]
                elif column == row:
                    triangle[row][column] = triangle[row][column] + triangle[row-1][column-1]
                else:
                    triangle[row][column] = triangle[row][column] + min(triangle[row-1][column], triangle[row-1][column-1])
        
        last_row = len(triangle) - 1
        min_path = float('inf')
        for column in range(len(triangle)):
            min_path = min(min_path, triangle[last_row][column])
        return min_path


triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle2 = [[-10]]

res = Solution()

print(res.minimumTotal(triangle1))
print(res.minimumTotal(triangle2))