class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxim=0
        for i in s:
            if i=='(':
                count+=1
                if count>maxim:
                    maxim=count
            elif i==')':
                count-=1
        return maxim
