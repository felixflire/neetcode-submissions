from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashList = {}

        key = set(sorted(nums))
        for i in key:
            if i not in hashList:
                hashList[i] = []
            for j in nums:
                if i == j :
                    hashList[i].append(j)

        # Sort dictionary keys by the length of their lists in descending order
        sorted_keys = sorted(hashList.keys(), key=lambda x: len(hashList[x]), reverse=True)
        # Take the first k elements from the sorted list of keys
        result = sorted_keys[:k]
        return result