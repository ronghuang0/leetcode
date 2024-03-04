# 984. Bag of Tokens

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        res = 0
        while tokens and (power >= tokens[0] or score>0):
            if power>=tokens[0]:
                power-=tokens[0]
                tokens.pop(0)
                score+=1
            else:
                power+=tokens[-1]
                tokens.pop()
                score-=1
            res = max(res, score)
        return res