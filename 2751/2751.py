# 2751. Robot Collisions

class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        arr = []
        for i in range(len(positions)):
            arr.append((positions[i], i))
        arr.sort()
        stack=[]
        for _, i in arr:
            if directions[i]=='R':
                stack.append(i)
            else:
                while stack:
                    lastI=stack.pop()
                    if healths[lastI] == healths[i]:
                        healths[lastI]=healths[i]=0
                        break
                    elif healths[lastI]>healths[i]:
                        healths[i]=0
                        healths[lastI]-=1
                        stack.append(lastI)
                        break
                    else:
                        healths[lastI]=0
                        healths[i]-=1
        res=[]
        for h in healths:
            if h>0:
                res.append(h)
        return res