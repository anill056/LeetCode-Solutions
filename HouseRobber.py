class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_robreward = 1
        max_robreward = max(nums)

        total_houses = len(nums)

        while min_robreward < max_robreward:
            mid_reward = (min_robreward + max_robreward) // 2
            possiblethefts = 0

            i = 0
            while i < total_houses:
                if nums[i] <= mid_reward:
                    possiblethefts += 1
                    i += 2
                else:
                    i += 1

            if k <= possiblethefts:
                max_robreward = mid_reward
            else:
                min_robreward = mid_reward + 1
            
        return min_robreward
