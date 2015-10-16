__author__ = 'bunny_gg'


class TreeNode:
    def __init__(self, api, parent, children=None, info=None, is_leaf=False, level = 1):
        self.parent = parent
        self.child = []
        self.add_children(children)
        self.info = []
        self.add_info(info)
        self.isLeaf = is_leaf
        self.api = api
        self.level = level

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.child.append(child)

    def add_children(self, children):
        if children != None:
            self.child.extend(children)

    def add_info(self, info):
        if info != None:
            self.info.extend(info)

    def set_api(self, api):
        self.api = api

    def set_is_leaf(self, is_leaf):
        self.isLeaf = is_leaf

    def set_level(self, level):
        self.set_level(level)