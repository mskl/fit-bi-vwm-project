import heapq as heap
from source.classes.MutableTuple import MutableTuple

class MyHeap:
    def __init__(self, target_k):
        self.__treshold = 10000
        self.__target_k = target_k
        self.minimum_heap = []
        self.max_key = 0

    # The key is the agregate value
    # The value points to an Automobile class instance
    # If there are less elements in the heap add the element for sure
    # Check the lowest element's key and if it is lower that the new one add the new one
    def add_element(self, element_key, element_value = None):
        if len(self.minimum_heap) < self.__target_k:
            self.__heap_push(element_key, element_value)
        else:
            lowest = self.heap_get_lowest()
            if element_key > lowest:
                self.__heap_pop_min()
                self.__heap_push(element_key, element_value)

    # ALG should end -> TRUE
    def set_treshold(self, new_treshold):
        # If the new treshold is lower than the lowest (= biggest) key in heap, return False
        if len(self.minimum_heap) != 0 and new_treshold < self.heap_get_lowest():
            return True
        self.__treshold = new_treshold
        return False

    def __heap_push(self, element_key, element_value):
        self.max_key = max(element_key, self.max_key)
        heap.heappush(self.minimum_heap, MutableTuple(element_key, element_value))

    def __heap_pop_min(self):
        heap.heappop(self.minimum_heap)

    def heap_get_lowest(self):
        return self.minimum_heap[0 ].key()

    def heap_get_biggest(self):
        return self.max_key

    def get_sorted_elements(self):
        return sorted(self.minimum_heap, reverse=True)

if __name__ == "__main__":
    # The target key
    mh = MyHeap(3)
    # Compute the treshold of all
    print(mh.set_treshold(100))
    mh.add_element(70)
    mh.add_element(80)
    mh.add_element(60)
    mh.add_element(71)
    print(mh.heap_get_lowest())
    print(mh.heap_get_biggest())
    mh.add_element(100)
    print(mh.heap_get_biggest())

