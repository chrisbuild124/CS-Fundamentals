# Impliment a Queue using two stacks
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

# The trick here is to use two stacks, and only reverse
# when one of the stacks is emptied, which will
# hardly ever occur, making each operation O(1) time. 

class MyQueue:

    def __init__(self):
        self.forward = []
        self.reverse = []

    def push(self, x: int) -> None:
        if not self.forward:
            while self.reverse:
                self.forward.append(self.reverse.pop())
        self.forward.append(x)

    def pop(self) -> int:
        if not self.reverse:
            while self.forward:
                self.reverse.append(self.forward.pop())
        return self.reverse.pop()

    def peek(self) -> int:
        if self.forward:
            return self.forward[0]
        else:
            return self.reverse[-1]

    def empty(self) -> bool:
        return False if self.reverse or self.forward else True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
