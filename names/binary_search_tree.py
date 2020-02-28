

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        # compare root node, if greater or equal go right
        if value >= self.value:
            # if no child
            if self.right == None:
                # insert
                self.right = BinarySearchTree(value)
            # else try again, continue right
            else:
                return self.right.insert(value)
        # if lesser go left
        elif value < self.value:
            # if no child
            if self.left == None:
                # insert
                self.left = BinarySearchTree(value)
            # else try again, continue left
            else:
                return self.left.insert(value)

    # else try again and repeat to left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
