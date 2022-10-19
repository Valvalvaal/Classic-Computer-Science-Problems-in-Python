from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs = 3

tower1 = Stack()
tower2 = Stack()
tower3 = Stack()

for i in range(num_discs):
    tower1.push(i+1)  # 3 discs, 1 to 3 1 beign the biggest

print(tower1)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)


hanoi(tower1, tower3, tower2, num_discs)

print(tower3)
