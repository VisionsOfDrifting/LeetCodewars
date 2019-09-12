"""
A quack is a data structure combining properties of both stacks and queues.
It can be viewed as a list of elements written left to right such that three
operations are possible:
    • push(x): add a new item x to the left end of the list
    • pop(): remove and return the item on the left end of the list
    • pull(): remove the item on the right end of the list.

Implement a quack using three stacks and O(1) additional memory, so that the
amortized time for any push, pop, or pull operation is O(1).
"""

"""
Let Q1, Q2, Q3 be the three stacks.
After N pushes Q1 = {1,2,3,4,5,6}
Transform it so that its divided equally among two stacks as {4,5,6} and {3,2,1}
For example :
Pop 3 elements into q2, and 3 into q3.
So Q2 = {6,5,4} Q3 = {3,2,1}
Pop back Q2 into Q1 , so that Q1 = {4,5,6}

Now, popFront() will take O(1), and its a pop on Q3.
Pop() will take O(1), and its a pop on Q1.
Push ()will take O(1) and its push on Q1.
"""


class Quack:
    def __str__(self):
        print(self.left)
        print(self.right)
        print(self.temp)
        return ''

    def __init__(self):
        self.left = []
        self.right = []
        self.temp = []

    def push(self, x):
        self.left.append(x)

    def pop(self):
        if not self.left and not self.right:
            raise IndexError('pop from empty quack')

        # Re-balance stacks
        if not self.left:
            self.balance(self.right, self.left)

        return self.left.pop()

    def pull(self):
        if not self.left and not self.right:
            raise IndexError('pull from empty quack')

        # Re-balance stacks
        if not self.right:
            self.balance(self.left, self.right)

        # If you really want to implement pull() as the question is stated remove the return
        return self.right.pop()

    def balance(self, primary, secondary):
        size = len(primary)
        # Move half of primary stack to buffer
        for _ in range(size // 2):
            self.temp.append(primary.pop())
        # Move remainder of primary to secondary
        while primary:
            secondary.append(primary.pop())
        # Move temp elements back to primary
        while self.temp:
            primary.append(self.temp.pop())


quack = Quack()

for i in range(6):
    quack.push(i + 1)

print(quack)
print(quack.pull())
print(quack)
print(quack.pop())
print(quack)
