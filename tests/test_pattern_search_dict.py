import unittest

from pattern_search.pattern_search_dict import PatternSearchDict


class NArySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = PatternSearchDict(get_names=lambda obj: obj['name'])

    def test_tree_initialization(self):
        self.assertIsInstance(self.tree, PatternSearchDict)

    def test_tree_pushed_item_is_searchable(self):
        item = {'name': 'natal'}
        self.tree.push(item)
        self.assertEqual(item, self.tree['nat'][0])

    def test_tree_allow_push_more_than_one_item(self):
        items = [{'name': 'natal'}, {'name': 'rio de janeiro'}]
        self.tree.push_items(items)
        self.assertEqual(items[0], self.tree['nat'][0])
        self.assertEqual(items[1], self.tree['rio'][0])


if __name__ == '__main__':
    unittest.main()
