class MinStack:
    def __init__(self):
        self.stack = []       # Main stack to store all elements
        self.min_stack = []   # Stack to track the minimum element

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or new val is <= current min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If top element is the current minimum, pop it from both stacks
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
