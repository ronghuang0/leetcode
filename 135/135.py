# 135. Candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        up=0
        down=0
        peak=1
        res=1
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                up+=1
                down=0
                peak=up+1
                res+=peak
            elif ratings[i]<ratings[i-1]:
                down+=1
                up=0
                res+=down
                if down>=peak:
                    res+=1
            else:
                peak=1
                up=0
                down=0
                res+=1
        return res