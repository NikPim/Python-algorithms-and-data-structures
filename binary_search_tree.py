class Node:
    def __init__(self, value):
        self.left = None
        self.right = None 
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    return self
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return self
                current_node = current_node.right


    def lookup(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def find_previous(self, value):
        current_node = self.root
        previous_node = current_node
        while current_node:
            if value == current_node.value:
                return previous_node
            elif value < current_node.value:
                previous_node = current_node
                current_node = current_node.left
            else:
                previous_node = current_node
                current_node = current_node.right


    def remove(self, value):
        prev_node = self.find_previous(value)
        node_to_remove = self.lookup(value)
        print(prev_node.value, node_to_remove.value)
        if node_to_remove.left and node_to_remove.right: #not finished, doesn't remove the succesor so it leads to duplicate value
            succesor = self.find_successor(node_to_remove.right)
            if prev_node.value < node_to_remove.value:
                prev_node.right = succesor
                prev_node.right.right = node_to_remove.right
                prev_node.right.left = node_to_remove.left
            else:
                prev_node.left = succesor
                prev_node.left.right = node_to_remove.right
                prev_node.left.left = node_to_remove.left
        elif node_to_remove.left and not node_to_remove.right:
            if prev_node.value < node_to_remove.value:
                prev_node.left = node_to_remove.left
            else:
                prev_node.right = node_to_remove.left
        elif not node_to_remove.left and node_to_remove.right:
            if prev_node.value < node_to_remove.value:
                prev_node.left = node_to_remove.right
            else:
                prev_node.right = node_to_remove.right
        else:
            if prev_node.value < node_to_remove.value:
                prev_node.right = None
            else:
                prev_node.left = None

    def find_successor(self, node):
        while True:
            if node.left == None:
                return node
            node = node.left


    def inorder_traversing(self, root):
        res = []
        if root:
            res = self.inorder_traversing(root.left)
            res.append(root.value)
            res = res + self.inorder_traversing(root.right)
        return res

bts = BinarySearchTree()

bts.insert(4)
bts.insert(6)
bts.insert(3)
bts.insert(2)
bts.insert(5)
bts.insert(12)
bts.insert(14)
bts.insert(19)
bts.insert(10)
bts.insert(13)
bts.insert(8)

print('     ', bts.root.value)
print(' ', bts.root.left.value,'     ', bts.root.right.value)
print(bts.root.left.left.value, '     ', bts.root.right.left.value, ' ', bts.root.right.right.value)
print('         ', bts.root.right.right.left.value,' ', bts.root.right.right.right.value)
print('        ',bts.root.right.right.left.left.value,'  ', bts.root.right.right.right.left.value, bts.root.right.right.right.right.value)

bts.remove(12)

print('     ', bts.root.value)
print(' ', bts.root.left.value,'     ', bts.root.right.value)
print(bts.root.left.left.value, '     ', bts.root.right.left.value, ' ', bts.root.right.right.value)
print('         ', bts.root.right.right.left.value,' ', bts.root.right.right.right.value)
print('        ',bts.root.right.right.left.left.value,'  ', bts.root.right.right.right.left.value, bts.root.right.right.right.right.value)