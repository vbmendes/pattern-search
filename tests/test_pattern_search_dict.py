#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from pattern_search.pattern_search_dict import PatternSearchDict


class NArySearchTree(unittest.TestCase):

    def setUp(self):
        self.cities = PatternSearchDict(get_names=lambda obj: obj['name'])

    def test_dict_initialization(self):
        self.assertIsInstance(self.cities, PatternSearchDict)

    def test_dict_pushed_item_is_searchable(self):
        item = {'name': 'natal'}
        self.cities.push(item)
        self.assertEqual(item, self.cities['nat'][0])

    def test_dict_allow_push_more_than_one_item(self):
        items = [{'name': 'natal'}, {'name': 'rio de janeiro'}]
        self.cities.push_items(items)
        self.assertEqual(items[0], self.cities['nat'][0])
        self.assertEqual(items[1], self.cities['rio'][0])

    def test_dict_setitem_is_similar_to_pushing_the_item_with_key_as_the_name_of_the_item(self):
        item = {'name': 'natal'}
        self.cities['natal'] = item
        self.assertEqual(item, self.cities['nat'][0])


if __name__ == '__main__':
    unittest.main()
