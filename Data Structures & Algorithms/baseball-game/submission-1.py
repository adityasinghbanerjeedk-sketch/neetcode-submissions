class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for char in operations:
            if char == '+' and len(score) > 1:
                score.append(score[-1] + score[-2])
            elif char == 'D' and len(score) > 0:
                score.append(score[-1] * 2)
            elif char == 'C' and len(score) > 0:
                score.pop()
            else:
                score.append(int(char))
        return sum(score)
        