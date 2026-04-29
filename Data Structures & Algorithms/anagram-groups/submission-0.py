class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashList = {}

        for i in strs:

            key = ''.join(sorted(i))
            if key not in  hashList:
                hashList[key] = []
            
            hashList[key].append(i)
            
        return list(hashList.values())
    
st = Solution()
print(st.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

        