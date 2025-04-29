import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

    def test_find_existing_node(self):
        node = self.tree._find(5, self.tree.root)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_find_nonexistent_node(self):
        node = self.tree._find(20, self.tree.root)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
