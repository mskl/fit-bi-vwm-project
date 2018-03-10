from source.classes.MyHeap import MyHeap
import unittest

class MyHeapTest(unittest.TestCase):
    def test_basic(self):
        h = MyHeap(3)
        self.assertEqual(h.set_treshold(100), False)
        h.add_element(70)
        h.add_element(80)
        h.add_element(65)
        self.assertEqual(h.heap_get_biggest(), 80)
        self.assertEqual(h.heap_get_lowest(), 65)
        h.add_element(68)
        self.assertEqual(h.heap_get_lowest(), 68)
        self.assertEqual(h.set_treshold(67), True)

    def test_sorted(self):
        h = MyHeap(3)
        self.assertEqual(h.set_treshold(100), False)
        h.add_element(70)
        h.add_element(80)
        h.add_element(65)
        self.assertEqual(h.get_sorted_elements(), [(80, None), (70, None), (65, None)])

    def test_ret_treshold(self):
        h = MyHeap(3)
        h.set_treshold(100)
        h.add_element(70)
        h.add_element(80)
        h.add_element(65)
        self.assertEqual(h.set_treshold(50), True)


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(MyHeapTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Run all the testing if ran from this file
if __name__ == '__main__':
    run_test()