import heapq as heap
from source.classes.MutableTuple import MutableTuple


class MyHeap:
    def __init__(self, target_k):
        self.__target_k = target_k
        self.__minimum_heap = []
        self.__treshold = 99999990
        self.max_value = 0

    def __heap_push(self, element_key, element_value):
        self.max_value = max(element_value, self.max_value)
        heap.heappush(self.__minimum_heap, MutableTuple(element_key.key(), element_value))

    def __heap_pop_min(self):
        return heap.heappop(self.__minimum_heap)

    # Add an element to the heap
    def add_element(self, element_key, element_value = None):
        # If there are less elements in the heap add the element for sure
        if len(self.__minimum_heap) < self.__target_k:
            self.__heap_push(element_key, element_value)
        else:
            # Check the lowest element's key and if it is lower that the new one add the new one
            if element_value > self.heap_get_lowest():
                self.__heap_pop_min()
                self.__heap_push(element_key, element_value)

    # ALG should end => TRUE
    def set_treshold(self, new_treshold):
        if len(self.__minimum_heap) == self.__target_k and new_treshold < self.heap_get_lowest():
            return True
        else:
            self.__treshold = new_treshold
            return False

    # Get the lowest value in O(1)
    def heap_get_lowest(self):
        return self.__minimum_heap[0].value()

    # Get the biggest value in O(1)
    def heap_get_biggest(self):
        return self.max_value

    # Sort the array and return it
    def get_sorted_elements(self):
        return sorted(self.__minimum_heap, reverse=True)

    # Get the unsorted heap
    def get_unsorted_heap(self):
        return self.__minimum_heap
