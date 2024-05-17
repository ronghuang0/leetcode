# 1146. Snapshot Array

class SnapshotArray:

    def __init__(self, length: int):
        # key: index of array
        # val: (snapshot, value at index)
        self.history=defaultdict(list)
        for i in range(length):
            self.history[i].append((0, 0))
        self.snapshots=0

    def set(self, index: int, val: int) -> None:
        # every time we set, we add to history map at index - (snap,val)
        self.history[index].append((self.snapshots, val))

    def snap(self) -> int:
        #increases snap
        self.snapshots+=1
        return self.snapshots-1

    def get(self, index: int, snap_id: int) -> int:
        # binary search at that index for last occurence of snap
        l=0
        r=len(self.history[index])-1
        while l<r:
            mid=(l+r+1)//2
            if self.history[index][mid][0]<=snap_id:
                l=mid
            else:
                r=mid-1
        return self.history[index][l][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)