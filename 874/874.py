# 874. Walking Robot Simulation

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x=0
        y=0
        d=0
        # n, e, s, w
        dirs=[(0,1), (1,0),(0,-1),(-1,0)]
        o=set()
        for obstacle in obstacles:
            o.add(tuple(obstacle))
        res=0
        for c in commands:
            if c==-1:
                d=(d+1)%4
            elif c==-2:
                d=(d+3)%4
            else:
                for i in range(c):
                    dx,dy=dirs[d]
                    nx = x+dx
                    ny = y+dy
                    if (nx,ny) in o:
                        break
                    x=nx
                    y=ny
                    res=max(res, x**2+y**2)
        return res