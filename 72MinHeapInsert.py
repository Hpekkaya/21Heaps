class MinHeap:
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
        # 1 Append the value to the heap
        self.heap.append(value)
        # 2 Set current index to the newly appended value
        current = len(self.heap) - 1
        # 3 create a loop to iterate over all the heap with 2 Cond
        #    Cond1 current > 0, Cond2 current.value < parent(current).value
        while current > 0 and self.heap[self._parent(current)] > self.heap[current]:
            # 31 swap(current, parent)
            self._swap(current, self._parent(current))
            # 32 set the parent to current
            current = self._parent(current)




myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)

print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

