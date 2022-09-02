class Solution:
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0
        
        # Naive Brute Force => Time Complexity - O(n^3) and Space Complexity - O(1)
        # res = self.brute_force(nums)
        # return res
        
        # Optimized Brute Force => Time Complexity - O(n^2) and Space Complexity - O(1)
        # res = self.optimized_brute_force(nums)
        # return res
        
        # Recursion => Time Complexity - O(n) and Space Complexity - O(n)
        # res = self.recursion(nums, len(nums)-1, 1)
        # return res
        
        # DP => Time Complexity - O(n) and Space Complexity - O(n)
        # res = self.dp(nums)
        # return res
        
        # DP Space Optimized => Time Complexity - O(n) and Space Complexity - O(1)
        res = self.dp_space_optimized(nums)
        return res
    
    
    def brute_force(self, nums):
        res = 0
        #l = []
        count = 0
        subarray_length = 3
        
        while subarray_length <= len(nums):
            for i in range(len(nums)):
                if i + subarray_length <= len(nums):
                    consider = True
                    for j in range(i+1, i+subarray_length-1):
                        if nums[j] - nums[j-1] != nums[j+1] - nums[j]:
                            consider = False
                            break
                    if consider:
                        #l.append(nums[i:i+subarray_length])
                        count += 1
            subarray_length += 1
        
        #print(l)
        return count
    
    def optimized_brute_force(self, nums):
        res = 0
        
        for i in range(len(nums)-2):
            difference = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == difference:
                    res += 1
                else:
                    break
        
        return res
    
    def recursion(self, nums, index, count):
        if index < 2:
            return 0
        
        if nums[index] - nums[index-1] == nums[index-1] - nums[index-2]:
            res = self.recursion(nums, index-1, count+1) + count
        else:
            res = self.recursion(nums, index-1, 1)
        
        return res
    
    def dp(self, nums):
        dp = [0] * len(nums)
        count = 1
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + count
                count += 1
            else:
                dp[i] = dp[i-1]
                count = 1
        
        return dp[-1]
    
    def dp_space_optimized(self, nums):
        dp = 0
        count = 1
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp = dp + count
                count += 1
            else:
                count = 1
        
        return dp

nums1 = [1,2,3,4]
nums2 = [0]
nums3 = [1,2,3,4,5,6]

res = Solution()

print(res.numberOfArithmeticSlices(nums1))
print(res.numberOfArithmeticSlices(nums2))
print(res.numberOfArithmeticSlices(nums3))