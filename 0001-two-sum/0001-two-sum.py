class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):   #This loop traverses each element from left to right
            for j in range(i+1,len(nums)):  # Inner loop to compare each number with outer
                if nums[i] + nums[j] == target:
                    return([i,j])