import unittest
from orderedlinkedlist import Orderedlinkedlist

class OrderedLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.oll = Orderedlinkedlist()

    def test_init(self):
        self.oll = Orderedlinkedlist([])
        self.oll = Orderedlinkedlist([1,2,3])
        self.oll = Orderedlinkedlist([-1,-2,-3])

    def test_size(self):
        self.assertEqual(self.oll.size(), 0)
        self.oll = Orderedlinkedlist([1,2])
        self.assertEqual(self.oll.size(), 2)

    def test_moins_size(self):
        self.oll.moins_size()
        self.assertEqual(self.oll.size(),0)
        self.oll = Orderedlinkedlist([1, 2])
        self.oll.moins_size()
        self.assertEqual(self.oll.size(),1)

    def test_plus_size(self):
        self.oll.plus_size()
        self.assertEqual(self.oll.size(), 1)
        self.oll.plus_size()
        self.oll.plus_size()
        self.oll.plus_size()
        self.assertEqual(self.oll.size(), 4)

    def test_first(self):
        self.assertEqual(self.oll.first(), None)

    def test_set_first(self):
        self.oll.set_first(self.oll.Node(12,1))

    def test_add(self):
        self.oll.add(self.oll.Node(12,1))
        self.assertEqual(self.oll.size(), 1)
        self.oll.add(self.oll.Node(12, 1))
        self.assertEqual(self.oll.size(), 2)

    def test_remove(self):
        self.oll.add(self.oll.Node(12, 1))
        self.oll.add(self.oll.Node(12, 1))
        self.oll.remove()
        self.assertEqual(self.oll.size(), 1)


if __name__ == '__main__':
    unittest.main()