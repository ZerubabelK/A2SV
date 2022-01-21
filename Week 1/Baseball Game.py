class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for op in ops:
            if op not in set(["C", "D", "+"]):
                op = int(op)
                record.append(op)
            else:
                if op == "C":
                    record.pop()
                elif op == "D":
                    record.append(record[-1] * 2)
                else:
                    score1 = record.pop()
                    score2 = record.pop()
                    record.extend([score2,score1,score1 + score2])
                print(record)
        return sum(record)