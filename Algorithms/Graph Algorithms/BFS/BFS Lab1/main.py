class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        break
                    else:
                        current_node = current_node.left_child
                elif value > current_node.value:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        break
                    else:
                        current_node = current_node.right_child

    def inorder_traversal(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left_child)
            print(node.value)
            traverse(node.right_child)
        traverse(self.root)

    def preorder_traversal(self):
        def traverse(node):
            if node is None:
                return
            print(node.value)
            traverse(node.left_child)
            traverse(node.right_child)
        traverse(self.root)

    def postorder_traversal(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left_child)
            traverse(node.right_child)
            print(node.value)
        traverse(self.root)

    def find_node(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def minimum_value(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.value

    def maximum_value(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node.value



    def remove_node(self, value):
        def remove(current_node, parent_node):
            # CASE 1: Leaf node
            if current_node.left_child is None and current_node.right_child is None:
                if current_node == self.root:
                    self.root = None
                elif current_node == parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

            # CASE 2: Node with one child
            elif current_node.left_child is None:
                if current_node == self.root:
                    self.root = current_node.right_child
                elif current_node == parent_node.left_child:
                    parent_node.left_child = current_node.right_child
                else:
                    parent_node.right_child = current_node.right_child

            elif current_node.right_child is None:
                if current_node == self.root:
                    self.root = current_node.left_child
                elif current_node == parent_node.left_child:
                    parent_node.left_child = current_node.left_child
                else:
                    parent_node.right_child = current_node.left_child

            # CASE 3: Node with two children
            else:
                successor_node = current_node.right_child
                while successor_node.left_child is not None:
                    successor_parent_node = successor_node
                    successor_node = successor_node.left_child

                current_node.value = successor_node.value
                remove(successor_node, successor_parent_node)

        if self.root is None:
            return False

        current_node = self.root
        parent_node = None
        while current_node is not None:
            if value == current_node.value:
                remove(current_node, parent_node)
                return True
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left_child
            else:
                parent_node = current_node
                current_node = current_node.right_child

        return False
'''

The remove_node() function takes a value to remove from the tree and first searches for the node with that value. If the node is not found, it returns False. Otherwise, it calls the remove() helper function, which handles all three cases:
If the node is a leaf node, simply remove it by setting the appropriate child of its parent to None.
If the node has one child, replace the node with its child by setting the appropriate child of its parent to the child.
If the node has two children, replace the node with its successor (i.e., the smallest value in its right subtree) by copying the successor's value into the node, and then recursively removing the successor node.
The time complexity of the remove_node() function is O(h), where h is the height of the tree. This is because it takes O(h)


'''



def merge_trees(tree1, tree2):
    def merge(current_node1, current_node2):
        if current_node1 is None and current_node2 is None:
            return None
        elif current_node1 is None:
            return current_node2
        elif current_node2 is None:
            return current_node1

        merged_node = Node(current_node1.value + current_node2.value)
        merged_node.left_child = merge(current_node1.left_child, current_node2.left_child)
        merged_node.right_child = merge(current_node1.right_child, current_node2.right_child)

        return merged_node

    merged_tree = BinarySearchTree()
    merged_tree.root = merge(tree1.root, tree2.root)

    return merged_tree

'''
The merge_trees() function takes two trees tree1 and tree2 as input and returns a new tree that is the merge of tree1 and tree2. To merge two trees, we simply need to add the values of the corresponding nodes in the two trees and create a new node in the merged tree with the sum as its value. We then recursively merge the left and right subtrees of the two trees to create the left and right subtrees of the merged tree.

The time complexity of the merge_trees() function is O(n), where n is the total number of nodes in the two trees. This is because we need to visit every node in both trees to merge them. The space complexity of the function is also O(n), since we need to create a new merged tree with all the nodes of the two input trees.
'''


  

bst = BinarySearchTree()

bst.insert_node(5)
bst.insert_node(3)
bst.insert_node(7)
bst.insert_node(2)
bst.insert_node(4)
bst.insert_node(6)
bst.insert_node(8)

print("inorder transversal")
bst.inorder_traversal()  # Outputs: 2 3 4 5 6 7 8
print(" ")
print("preorder transversal")
bst.preorder_traversal()
print(" ")
print("postorder transversal")
bst.postorder_traversal()
print(" ")
node = bst.find_node(6)
print(node.value)  # Outputs: 6
print(" ")
print("minimum value")
print(bst.minimum_value())  # Outputs: 2
print(" ")
print("maximum value")
print(bst.maximum_value())  # Outputs: 8

bst.remove_node(4)
print(" ")
print("inorder transversal post remove")
bst.inorder_traversal()




bstb = BinarySearchTree()
bstb.insert_node(5)
bstb.insert_node(3)
bstb.insert_node(7)
print(" ")
print("inorder transversal")
bstb.inorder_traversal()
print(" ")
merge_trees(bst, bstb)
print("inorder transversal post merge")
bst.inorder_traversal()

print(" ")
bstc = BinarySearchTree()

bstc.insert_node(5)
bstc.insert_node(3)
bstc.insert_node(7)
print("inorder transversal")
bstc.inorder_traversal()
print(" ")
bstc.remove_node(3)
print("inorder transversal")
bstc.inorder_traversal()
print(" ")



bstd = BinarySearchTree()
keys = [15, 10, 20, 8, 12, 16, 13, 7, 3, 4]
root = None
for key in keys:
    root = bstd.insert_node(key)
print("inorder transversal")
bstd.inorder_traversal()
