# 155
# TC : O(1)


class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.data.append((val, val))
        else:
            temp_min = min(val, self.data[-1][1])
            self.data.append((val, temp_min))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
