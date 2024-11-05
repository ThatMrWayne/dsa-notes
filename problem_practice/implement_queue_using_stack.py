# 232


class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.pop_stack:
            result = self.pop_stack.pop()
        else:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
            result = self.pop_stack.pop()
        return result

    def peek(self) -> int:
        if self.pop_stack:
            result = self.pop_stack[-1]
        else:
            result = self.push_stack[0]
        return result

    def empty(self) -> bool:
        result = True if (len(self.pop_stack) + len(self.push_stack) == 0) else False
        return result
