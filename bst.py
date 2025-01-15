"""
bst file
"""

from node import Node

class BinarySearchTree():
    """
    my BinarySearchTree class
    """
    def __init__(self):
        """
        init function
        """
        self.root = None
        self.size = 0

    def insert(self, key, value):
        """
        my public insert function
        """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)


    @staticmethod
    def _insert(key, value, node):
        """
        my private insert function
        """
        if key < node:
            if node.has_left_child():
                BinarySearchTree._insert(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        elif key > node:
            if node.has_right_child():
                BinarySearchTree._insert(key, value, node.right)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value


    def inorder_traversal_print(self):
        """
        my public print function
        """
        self._print_nodes(self.root)

    @staticmethod
    def _print_nodes(node):
        """
        my private insert function
        """
        if node is None:
            return
        if node.has_left_child():
            BinarySearchTree._print_nodes(node.left)

        print(node.value)
        if node.has_right_child():
            BinarySearchTree._print_nodes(node.right)

    def get(self, key):
        """
        my public get function
        """
        if self.root is not None:
            return self._get(key, self.root)
        raise KeyError("not a valid key")

    def _get(self, key, cur_node):
        """
        my private get function
        """
        if key == cur_node.key:
            return cur_node.value
        elif key < cur_node.key and cur_node.left is not None:
            return self._get(key, cur_node.left)
        elif key > cur_node.key and cur_node.right is not None:
            return self._get(key, cur_node.right)
        raise KeyError("Not a valid key")



    def remove(self, key):
        """
        my public remove function
        """
        if self.find(key) is None:
            raise KeyError("Not found")
        return self.find(key).value
        self._remove(self.find(key))


    def find(self, key):
        """
        my public find function to remove function
        """
        if self.root is not None:
            return self._find(key, self.root)
        return None

    def _find(self, key, cur_node):
        """
        my private find function
        """
        if key == cur_node.key:
            return cur_node
        elif key < cur_node.key and cur_node.left is not None:
            return self._find(key, cur_node.left)
        elif key > cur_node.key and cur_node.right is not None:
            return self._find(key, cur_node.right)


    def _remove(self, node):
        """
        my private remove function
        """

        def min_value_node(curr_n):
            """
            my public min_value_node function
            """
            current = curr_n
            while current.left is not None:
                current = current.left
            return current

        def num_children(children):
            """
            my public num_children function
            """
            num_children = 0
            if children.left is not None:
                num_children += 1
            if children.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        # Node has no children
        if node_children == 0:
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # Node has a single child
        if node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            child.parent = node_parent

        # node has two children
        if node_children == 2:
            successor = min_value_node(node.right)
            node.value = successor.value
            self._remove(successor)



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(11, "banan")
    bst.insert(6, "äpple")
    bst.insert(8, "jordgubb")
    bst.insert(12, "morot")
    bst.inorder_traversal_print()
    print("första print\n")
    print(bst.get(11))
    print("första Get\n")
    bst.remove(8)
    print("första del")
    bst.inorder_traversal_print()
