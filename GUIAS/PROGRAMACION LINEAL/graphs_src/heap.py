class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def extract_max(self):
        if self.size == 0:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down(0)
        return max_value

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)