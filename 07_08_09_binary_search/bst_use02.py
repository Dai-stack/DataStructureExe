# 章末問題用
import bst

## bstを構築(問題7.4)
root = bst.Node(25)

root.left = bst.Node(6)
root.right = bst.Node(49)

root.left.left = bst.Node(2)
root.right.left = bst.Node(28)
root.right.right = bst.Node(65)

root.right.right.left = bst.Node(51)
root.right.right.right = bst.Node(66)

root.right.right.right.right = bst.Node(78)

root.right.right.right.right.left = bst.Node(88)

bst = bst.BST()

bst.display(root)

print("\n")
print("行き掛け順:")

bst.preorder(root)

print("\n")
print("通り掛け順:")
bst.inorder(root)

print("\n")
print("帰り掛け順:")
bst.postorder(root)

print("\n")
print("最小ノード値:", bst.find_min_node(root))

print("\n")
print("最大ノード値:", bst.find_max_node(root))

print("\n")
print("ノード数:", bst.find_tree_size(root))

print("\n")
print("ツリーの高さ:", bst.find_height(root))
