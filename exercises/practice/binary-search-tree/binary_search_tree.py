class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self._tree_data = tree_data

    def data(self):
        if len(self._tree_data) == 1:
            return TreeNode(self._tree_data[0])

        root = self._tree_data[0]
        tree = TreeNode(root)

        for num in self._tree_data[1:]:
            if num <= root:
                tree.left = TreeNode(num)
            else:
                tree.right = TreeNode(num)

        print(tree)
        return tree

    def sorted_data(self):
        pass
