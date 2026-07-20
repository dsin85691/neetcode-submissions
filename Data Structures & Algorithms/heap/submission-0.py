class MinHeap:

    def __init__(self):
        self.heap = []

    def percolate_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self.heap[parent] <= self.heap[idx]:
                break

            self.heap[parent], self.heap[idx] = \
                self.heap[idx], self.heap[parent]

            idx = parent

    def percolate_down(self, idx):
        n = len(self.heap)

        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = \
                self.heap[smallest], self.heap[idx]

            idx = smallest

    def push(self, val):
        self.heap.append(val)
        self.percolate_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return -1

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.percolate_down(0)

        return root

    def top(self):
        if not self.heap:
            return -1
        return self.heap[0]

    def heapify(self, nums):
        self.heap = nums[:]

        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.percolate_down(i)