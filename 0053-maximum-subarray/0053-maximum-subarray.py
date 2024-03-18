class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 
        solution, tempsum = nums[0], nums[0]
        # loop to check which subarray satisfies the condition
        for i in range(1, len(nums)):
            tempsum = max(tempsum + nums[i], nums[i])
            if tempsum > solution:
                solution = tempsum
        return solution