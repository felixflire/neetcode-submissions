from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashlist = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashlist:
                return [hashlist[complement], i]
            hashlist[nums[i]] = i


ts = Solution()
print(ts.twoSum([2,7,11,15], 9))


        