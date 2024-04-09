class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # 1 Append the value at the end of heap
        self.heap.append(value)
        # 2 Set the current to index of newly appended value
        current = len(self.heap) - 1
        # 3 Create while loop
        # (Cond1 : index(current) >0  Cond2 current.value > parent.value
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            # 31 swap current, parent
            self._swap(current, self._parent(current))
            # 32 update current for next iteration
            current = self._parent(current)




myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)


myheap.insert(100)

print(myheap.heap)


myheap.insert(75)

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""