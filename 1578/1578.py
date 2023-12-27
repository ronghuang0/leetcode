class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        sum = 0
        big = 0
        for i in range(len(colors)):
            if i!=0 and colors[i] != colors[i-1]:
                res+=sum-big
                sum=0
                big=0
            sum+=neededTime[i]
            big=max(big,neededTime[i])
        res+=sum-big
        return res