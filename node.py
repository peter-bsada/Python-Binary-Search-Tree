"""
My node file
"""

class Node():
    """
    My node class
    """
    def __init__(self, key, value, parent=None):
        """
        My init function
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def has_left_child(self):
        """
        my public has_left_child function
        """
        return self.left is not None

    def has_right_child(self):
        """
        my public has_right_child function
        """
        return self.right is not None

    def __lt__(self, other):
        """
        my lt function
        """
        if isinstance(other, Node):
            return self.key < other.key
        return self.key < other

    def __gt__(self, other):
        """
        my gt function
        """
        if isinstance(other, Node):
            return self.key > other.key
        return self.key > other

    def __eq__(self, other):
        """
        My eq function
        """
        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other
