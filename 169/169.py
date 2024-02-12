# 169. Majority Element

# Boyer-Moore Voting Algorithm
# O(n) time O(1) space
class Solution:
    def majorityElement(self, nums) -> int:
        curr = None
        count = 0
        for n in nums:
            if count == 0:
                curr = n
                count+=1
                continue
            if curr == n:
                count+=1
            else:
                count-=1
        return curr