import json


class PatternSearchDict(dict):

    def __init__(self, get_names):
        self.get_names = get_names

    def _get_names(self, obj):
        names = self.get_names(obj)
        if hasattr(names, '__iter__'):
            return names
        else:
            return [names]

    def push(self, obj):
        """
        Pushes a new object in the tree.
        """
        for name in self._get_names(obj):
            for i in xrange(1, len(name) + 1):
                tree_node = self.setdefault(name[:i], [])
                tree_node.append(obj)

    def push_items(self, items):
        for obj in items:
            self.push(obj)


if __name__ == '__main__':
    cities = json.loads(open('./fixtures/cities.json').read())
    tree = Tree(key_names=['nome'])
    for city in cities:
        tree.push(city)
    tree = Tree.from_items(cities)
    natal = tree['natal']
