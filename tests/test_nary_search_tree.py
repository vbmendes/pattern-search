import unittest

from pattern_search.nary_search_tree import Tree, Node

class NodeTestCase(unittest.TestCase):
    
    def test_node_initialization(self):
        node = Node()
        self.assertEqual(node.items, [])
        self.assertEqual(node.children, {})
    
    def test_node_add_item(self):
        node = Node()
        node.add_item('item')
        self.assertEqual(node.items, ['item'])
    
    def test_node_add_two_items(self):
        node = Node()
        node.add_item('item1')
        node.add_item('item2')
        self.assertEqual(node.items, ['item1', 'item2'])

class NArySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.tree = Tree()
    
    def test_tree_initialization(self):
        self.assertIsInstance(self.tree.root, Node)
    
    def test_push_pattern_a(self):
        self.tree.push('a')
        self.assertIn('a', self.tree.root.children)
    
    def test_push_pattern_ab(self):
        self.tree.push('ab')
        self.assertIn('a', self.tree.root.children)
        self.assertIn('b', self.tree.root.children['a'].children)
    
    def test_push_pattern_a_then_pattern_ab_then_pattern_ac(self):
        self.tree.push('a')
        self.tree.push('ab')
        self.tree.push('ac')
        self.assertIn('a', self.tree.root.children)
        self.assertIn('b', self.tree.root.children['a'].children)
        self.assertIn('c', self.tree.root.children['a'].children)
    
    def test_search_in_empty_tree_returns_empty_list(self):
        self.assertEqual(self.tree.search('pattern'), [])
    
    def test_push_vinicius_and_search_for_vin_is_not_empty(self):
        pushed_value = {'name': 'Vinicius', 'age': 25}
        self.tree.push('vinicius', pushed_value)
        returned_value = self.tree.search('vin') 
        self.assertTrue(returned_value)
        self.assertEqual(returned_value[0]['name'], pushed_value['name'])
    
    def test_push_vinicius_and_search_for_ini_is_empty(self):
        pushed_value = {'name': 'Vinicius', 'age': 25}
        self.tree.push('vinicius', pushed_value)
        returned_value = self.tree.search('ini') 
        self.assertEqual(returned_value, [])
    
    def test_push_vinicius_and_vinicolas_and_search_vini_returns_both_items(self):
        pushed_vinicius = {'name': 'Vinicius', 'age': 25}
        pushed_vinicolas = {'name': 'Vinicolas', 'age': 23}
        self.tree.push('vinicius', pushed_vinicius)
        self.tree.push('vinicolas', pushed_vinicolas)
        returned_value = self.tree.search('vin')
        self.assertEqual(returned_value[0]['name'], pushed_vinicius['name'])
        self.assertEqual(returned_value[1]['name'], pushed_vinicolas['name'])


if __name__ == '__main__':
    unittest.main()