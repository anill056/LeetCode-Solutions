class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0 #[-2] for ex
        result = nums[0]

        for num in nums:
            if total < 0:
                total = 0

            total += num
            result = max(result,total)

        return result