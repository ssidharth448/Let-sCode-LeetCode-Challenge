class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        flag=0
        for i in nums:
            flag+=i
            if flag==0:
                count+=1
        return count
