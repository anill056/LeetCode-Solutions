class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return []

        nums.sort()

        k = 0 

        for j in range(1,len(nums)):
            if(nums[j] != nums[k]):
                k += 1
                nums[k] = nums[j]

        return k+1