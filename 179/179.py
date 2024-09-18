# 179. Largest Number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a,b):
            a=str(a)
            b=str(b)
            if (a+b) > (b+a):
                return -1
            return 1
        
        nums.sort(key=cmp_to_key(comp))
        res=''
        for num in nums:
            res+=str(num)
        if res[0]=='0':
            return '0'
        return res