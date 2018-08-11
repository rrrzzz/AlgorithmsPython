from Heap.HeapStructure import Heap, get_parent_index


class PriorityQueue(Heap):
    def __init__(self, array):
        assert isinstance(array, list)
        Heap.__init__(self, array)

    def get_max_element(self):
        if self.heap_size < 1:
            raise ValueError("Heap is empty")

        return self[1]

    def extract_max_element(self):
        if self.heap_size < 1:
            raise ValueError("Heap is empty")

        maximum = self.heap_array[1]
        self[1] = self[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)
        return maximum

    def increase_key(self, index, key):
        if self[index] > key:
            raise ValueError(f"The value {self[index]}"
                             f" in heap at index {index}"
                             f" is larger than key {key}")

        while index > 1 and self[get_parent_index(index)] < key:
            self[index] = self[get_parent_index(index)]
            index = get_parent_index(index)

        self[index] = key

    def insert_key(self, key):
        self.heap_size += 1
        self.heap_array.append(key)
        self.increase_key(self.heap_size, key)
