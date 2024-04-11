# 950. Reveal Cards in Increasing Order

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        deckIndex = 0
        res = [0]*n
        resIndex = 0
        skip = False
        while deckIndex < n:
            if res[resIndex] == 0:
                if not skip:
                    res[resIndex] = deck[deckIndex]
                    deckIndex+=1
                skip = not skip
            resIndex = (resIndex+1)%n
        return res