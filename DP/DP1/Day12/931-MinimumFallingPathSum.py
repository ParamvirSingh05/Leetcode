class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # Recursive => Time Complexity - O(n * 3^n) and Space Complexity - O(n) - It gives TLE
        # Memoization => Time Complexity - O(n^2) and Space Complexity - O(n^2)
        # min_path = float('inf')
        # dp = [[None for _ in range(len(matrix))] for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     temp = self.recursive(matrix, 0, i, dp)
        #     min_path = min(temp, min_path)
        # return min_path
        
        # Tabulation => Time Complexity - O(n^2) and Space Complexity - O(n^2)
        #return self.tabulation(matrix)
        
        # Tabulation Space Optimized - Time Complexity - O(n^2) and Space Complexity - O(n)
        return self.space_optimized(matrix)
    
    def recursive(self, matrix, row, column, dp):
        if row == len(matrix)-1:
            return matrix[row][column]
        
        # left_diagonal = matrix[row+1][column-1]
        # right_diagonal = matrix[row+1][column+1]
        # bottom = matrix[row+1][column]
        if dp[row][column] != None:
            return dp[row][column]
        
        left_diagonal = True if column != 0 else False
        right_diagonal = True if column != len(matrix)-1 else False
        
         
        if left_diagonal and right_diagonal:
            min_path = matrix[row][column] + min(self.recursive(matrix, row+1, column-1, dp),
                                            self.recursive(matrix, row+1, column, dp),
                                            self.recursive(matrix, row+1, column+1, dp))
        elif left_diagonal:
            min_path = matrix[row][column] + min(self.recursive(matrix, row+1, column-1, dp),
                                            self.recursive(matrix, row+1, column, dp))
        elif right_diagonal:
            min_path = matrix[row][column] + min(self.recursive(matrix, row+1, column, dp),
                                            self.recursive(matrix, row+1, column+1, dp))
        dp[row][column] = min_path
        
        return min_path
    
    def tabulation(self, matrix):
        dp = [[None for _ in range(len(matrix))] for _ in range(len(matrix))]
        for col in range(len(matrix)):
            dp[0][col] = matrix[0][col]
        
        for row in range(1, len(matrix)):
            for column in range(len(matrix)):
                if column == 0:
                    dp[row][column] = matrix[row][column] + min(dp[row-1][column], dp[row-1][column+1])
                elif column == len(matrix) - 1:
                    dp[row][column] = matrix[row][column] + min(dp[row-1][column], dp[row-1][column-1])
                else:
                    dp[row][column] = matrix[row][column] + min(dp[row-1][column], dp[row-1][column-1], dp[row-1][column+1])
        
        min_path = float('inf')
        last_row = len(matrix) - 1
        for column in range(len(matrix)):
            min_path = min(min_path, dp[last_row][column])
        
        return min_path
    
    def space_optimized(self, matrix):
        prev_row = [matrix[0][column] for column in range(len(matrix))]
        for row in range(1, len(matrix)):
            current_row = []
            for column in range(len(matrix)):
                if column == 0:
                    current_row.append(matrix[row][column] + min(prev_row[column], prev_row[column+1]))
                elif column == len(matrix) - 1:
                    current_row.append(matrix[row][column] + min(prev_row[column], prev_row[column-1]))
                else:
                    current_row.append(matrix[row][column] + min(prev_row[column], prev_row[column-1], prev_row[column+1]))
            prev_row = current_row
        
        return min(prev_row)

matrix1 = [[2,1,3],[6,5,4],[7,8,9]]
matrix2 = [[-19,57],[-40,-5]]

res = Solution()
print(res.minFallingPathSum(matrix1))
print(res.minFallingPathSum(matrix2))