def heap_sort(items_list):
    if len(items_list) < 2:
        return

    heap_list = Heap(items_list)

    while heap_list.heap_size > 1:
        heap_list.swap_items(1, heap_list.heap_size)
        heap_list.heap_size -= 1
        heap_list.max_heapify(1)


def get_parent_index(index):
    return index >> 1


def get_left_child_index(index):
    return index << 1


def get_right_child_index(index):
    return (index << 1) + 1


class Heap:
    def __init__(self, array):
        assert isinstance(array, list)
        self.heap_array = array
        self.heap_size = len(array)
        self.build_max_heap()

    def __getitem__(self, key):
        return self.heap_array[key - 1]

    def __setitem__(self, key, value):
        self.heap_array[key - 1] = value

    def swap_items(self, first_index, second_index):
        temp = self[first_index]
        self[first_index] = self[second_index]
        self[second_index] = temp

    def max_heapify(self, parent_index):
        while True:
            left = get_left_child_index(parent_index)
            right = get_right_child_index(parent_index)
            largest = parent_index

            if left <= self.heap_size and self[left] > self[largest]:
                largest = left

            if right <= self.heap_size and self[right] > self[largest]:
                largest = right

            if largest != parent_index:
                self.swap_items(parent_index, largest)
                parent_index = largest
            else:
                return

    def build_max_heap(self):
        start_index = self.heap_size // 2

        for i in range(start_index, 0, -1):
            self.max_heapify(i)
