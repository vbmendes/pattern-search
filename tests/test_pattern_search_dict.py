import unittest

from pattern_search.pattern_search_dict import PatternSearchDict


class NArySearchTree(unittest.TestCase):

    def setUp(self):
        self.dict = PatternSearchDict(get_names=lambda obj: obj['name'])

    def test_dict_initialization(self):
        self.assertIsInstance(self.dict, PatternSearchDict)

    def test_dict_pushed_item_is_searchable(self):
        item = {'name': 'natal'}
        self.dict.push(item)
        self.assertEqual(item, self.dict['nat'][0])

    def test_dict_allow_push_more_than_one_item(self):
        items = [{'name': 'natal'}, {'name': 'rio de janeiro'}]
        self.dict.push_items(items)
        self.assertEqual(items[0], self.dict['nat'][0])
        self.assertEqual(items[1], self.dict['rio'][0])

    def test_dict_setitem_is_similar_to_pushing_the_item_with_key_as_the_name_of_the_item(self):
        item = {'name': 'natal'}
        self.dict['natal'] = item
        self.assertEqual(item, self.dict['nat'][0])


if __name__ == '__main__':
    unittest.main()
