"""
Filename:linkedbst.py
"""

from AbstractCollection import AbstractCollection
from linkedbst.bstnode import BSTNode
from Queue.LinkedQueue import LinkedQueue
from Stack.LinkedStack import LinkedStack

class LinkedBST(AbstractCollection):
    """A link-based binary search tree implementation."""

    def __init__(self,sourveCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root=None
        AbstractCollection.__init__(self,sourveCollection)

    def find(self,item):
        """
        Returns data if item is found or None otherwise

        if the tree is empty
            return None
        else if the target item equals the root item
            return the root item
        else if the target item is less than the root item
            return the result of searching the left subtree
        else
            return the result of searching the right subtree
        """
        # Helper fuction to search the binary tree
        def recurse(node):
            if node is None:
                return False
            elif item==node.data:
                return node.data
            elif item<node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        # Top-level call on the root node
        return recurse(self._root)

    def inorder(self):
        """
        Supports an inorder traversal on a view of self.
        Returns the list of inorder results

        if the tree is not empty
            visit the left subtree
            visit the item at the top of the tree
            visit the right subtree
        """
        lyst=list()
        def recurse(node):
            if node!=None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        lyst=list()
        def recurse(node):
            if node!=None:
                recurse(node.left)
                recurse(node.righ)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        lyst=list()
        queue=LinkedQueue()
        if self._root==None:
            return None
        else:
            queue.add(self._root)
            def recurse():
                if not queue.isEmpty():
                    result=queue.pop()
                    lyst.append(result.data)
                    queue.add(result.left)
                    queue.add(result.right)
                    recurse()
        return iter(lyst)

    def __iter__(self):
        """
        We use this function frequently so if we use the method that inorder and postorder take,
        the algorithm will take a linear operation time and linear Ram.Because both of them use iteration.
        So, when using __iter__, we use a generator to improve this situation.
        """
        stack=LinkedStack()
        if self._root == None:
            return None
        else:
            stack.push(self._root)
            while not stack.isEmpty():
                result=stack.pop()
                yield result.data
                stack.push(result.right)
                stack.push(result.left)

    def __str__(self):
        """Returns a string representation with the tree rotated 90 degrees counterclockwise."""
        def recurse(node,level):
            s=""
            if node!=None:
                s+=recurse(node.right,level+1)
                s+="|"*level
                s+=str(node.data)+"\n"
                s+=recurse(node.left,level+1)
            return s
        return recurse(self._root,level=0)

    def add(self,item):
        """Adds item to the tree."""

        #Helper fuction to search for item's posiiton.
        def recurse(node):
            #New item is less; go left until spot is found
            if item<node.data:
                if node.left==None:
                    node.left=BSTNode(item)
                else:
                    recurse(node.left)
            elif node.right==None:
                node.right=BSTNode(item)
            else:
                recurse(node.right)

        if self.isEmpty():
            self._root=BSTNode(item)
        else:
            recurse(self._root)
        self._size+=1

    def delete(self,item):
        cursor = None
        reference = ""
        def search(node):
            global cursor
            global reference

            if node.data==item:
                return cursor,reference
            elif node.data>item:
                cursor=node
                reference="left"
                search(node.left)
            else:
                cursor=node
                reference="right"
                search(node.right)

        cursor,reference=search(self._root)
        if cursor==None:
            """The root need to be delete"""
            self._root=None
        elif



self._size-=1







