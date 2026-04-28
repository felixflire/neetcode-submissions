from typing import List

class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
            hashset = {}

            for i in nums:
                if i in hashset:
                    return True
                hashset[i] = True

            return False
s1 = Solution()
print(s1.hasDuplicate([1,2,3,4,5,5,6]))