import json


class PatternSearchDict(dict):

    def __init__(self, get_names):
        self.get_names = get_names

    def __setitem__(self, key, obj):
        for i in xrange(1, len(key) + 1):
            tree_node = self.setdefault(key[:i], [])
            tree_node.append(obj)

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
            self[name] = obj

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
