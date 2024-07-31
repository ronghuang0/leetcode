# 1653. Minimum Deletions to Make String Balanced

class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp=[0]*(len(s)+1) #num of a's before
        count=0
        for i in range(1,len(s)+1):
            if s[i-1]=='a':
                count+=1
            dp[i]=count
        numBBefore=[0]*len(s)
        numAAfter=[0]*len(s)
        for i in range(len(s)):
            # keeping s[i]
            # if a - num of B's before + num of a's after
            # if b - num of b's before + num of a's after
            numBBefore[i] = i-dp[i]
            numAAfter[i] = dp[len(s)]-dp[i+1]
        ans=float('inf')
        for i in range(len(s)):
            ans=min(ans, numBBefore[i]+numAAfter[i])
        return ans