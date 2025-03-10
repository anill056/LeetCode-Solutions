class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: #Base Case
            return []

        newnums = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    newnums.append(f"{start}")
                else:
                    newnums.append(f"{start}->{nums[i-1]}")
        
                start = nums[i]
        
        if start == nums[-1]:
           newnums.append(f"{start}")
        else:
            newnums.append(f"{start}->{nums[-1]}")  

        return newnums  
        

