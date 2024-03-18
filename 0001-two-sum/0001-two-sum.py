class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} #Dictionary to store key value pairs 
        for i in range(len(nums)):  #Using single loop to find the complement and insert element to reduce complexity. 
            o = target - nums[i]
            if o in d:
                return([i,d[o]])  #if element's complement exists return the index
            d[nums[i]] = i