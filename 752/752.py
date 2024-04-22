# 752. Open the Lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        d = set(deadends)
        if '0000' in d:
            return -1
        count=0
        visited=set('0000')
        q = ['0000']
        while q:
            next=[]
            for node in q:
                if node == target:
                    return count
                for i, char in enumerate(node):
                    above = node[0:i]+str((int(char)+1)%10)+node[i+1:]
                    below = node[0:i]+str((int(char)-1)%10)+node[i+1:]
                    if above not in d and above not in visited:
                        next.append(above)
                        visited.add(above)
                    if below not in d and below not in visited:
                        next.append(below)
                        visited.add(below)
            count+=1
            q=next
        return -1