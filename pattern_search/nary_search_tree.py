#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    
    def __init__(self):
        self.items  = []
        self.children = {}
    
    def add_item(self, item):
        self.items.append(item)


class Tree(object):
    
    def __init__(self):
        self.root = Node()

    def push(self, pattern, item=True):
        node = self.root
        for char in pattern:
            next_node = node.children.setdefault(char, Node())
            next_node.add_item(item)
            node = next_node
        
    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return node.items
        
