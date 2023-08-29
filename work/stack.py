class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        top = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        top = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2
