class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool: // hashmap method
    #     freqMap = {}
    #     flag=False

    #     for i in nums:
    #         freqMap[i] = freqMap.get(i, 0) + 1

    #     for j in freqMap.values():
    #         if j>1:
    #             flag=True
        
    #     return flag

    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for num in nums:
            if num in uniqueNums:
                return True
            uniqueNums.add(num)
        return False
        