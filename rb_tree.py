
class RBNode(object):

    def __init__(self, color: int=None, value: object=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color  # 0 red, 1 black
        self.value = value

    def __str__(self):
        return f"value:{self.value} color:{self.color}"

    __repr__ = __str__


class RBTree(object):

    def __init__(self):
        self.root = RBNode()

    def _search(self, node, value):

        if node is None:
            return None

        if node.value > value:
            self._search(node.right, value)

        elif node.value < value:
            self._search(node.left, value)

        else:
            return node

    def search(self, value):

        if self.root.value == None:
            return None

        return self._search(self.root, value)

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def __str__(self):
        pass


def main():
    tree = RBTree()
    print(tree.search(10))


if __name__ == "__main__":
    main()
