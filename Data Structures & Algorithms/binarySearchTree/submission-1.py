from typing import List

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:

        def helper(root, key, val):
            if not root:
                return Node(key, val)

            if key > root.key:
                root.right = helper(root.right, key, val)

            elif key < root.key:
                root.left = helper(root.left, key, val)

            else:
                # key already exists → update value
                root.val = val

            return root

        self.root = helper(self.root, key, val)


    def get(self, key: int) -> int:

        curr = self.root

        while curr:

            if key > curr.key:
                curr = curr.right

            elif key < curr.key:
                curr = curr.left

            else:
                return curr.val

        return -1


    def getMin(self) -> int:

        if not self.root:
            return -1

        curr = self.root

        while curr.left:
            curr = curr.left

        return curr.val      # changed


    def getMax(self) -> int:

        if not self.root:
            return -1

        curr = self.root

        while curr.right:
            curr = curr.right

        return curr.val      # changed


    def remove(self, key: int) -> None:

        def helper(root, key):

            if not root:
                return None

            if key < root.key:
                root.left = helper(root.left, key)

            elif key > root.key:
                root.right = helper(root.right, key)

            else:
                # Case 1: no left child
                if not root.left:
                    return root.right

                # Case 2: no right child
                if not root.right:
                    return root.left

                # Case 3: two children
                successor = root.right

                while successor.left:
                    successor = successor.left

                root.key = successor.key
                root.val = successor.val

                root.right = helper(root.right, successor.key)

            return root

        self.root = helper(self.root, key)


    def getInorderKeys(self) -> List[int]:

        inorder_list = []

        def inorder(node):

            if not node:
                return

            inorder(node.left)
            inorder_list.append(node.key)
            inorder(node.right)

        inorder(self.root)

        return inorder_list