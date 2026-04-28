class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        ans = []

        for i in range(2*size):
            if i<size:
                ans.append(nums[i])
            else:
                ans.append(nums[i-size])
        
        return ans
        