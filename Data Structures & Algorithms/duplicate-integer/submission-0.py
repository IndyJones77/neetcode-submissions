class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        flag=False

        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1

        for j in freqMap.values():
            if j>1:
                flag=True
        
        return flag
        