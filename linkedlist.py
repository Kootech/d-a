class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None


def main():
    lnklist = LinkedList()
    lnklist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #link nodes
    lnklist.head.next = second
    second.next = third



