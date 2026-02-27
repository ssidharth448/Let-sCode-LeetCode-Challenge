class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        n=0
        for i in nums:
            if i%2==0 and i%3==0:
                sum+=i
                n+=1
        if n!=0:
            return sum//n
        return 0
