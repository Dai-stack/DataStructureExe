# レベルゼロ（ルート）
import bst

root = bst.Node(40)

# レベル１
root.left = bst.Node(30)
root.right = bst.Node(70)

# レベル2
root.left.left = bst.Node(10)
root.left.right = None
root.right.left = bst.Node(60)
root.right.right = bst.Node(90)

# レベル3
root.left.left.left = None
root.left.left.right = bst.Node(20)
root.right.left.left = None
root.right.left.right = None
root.right.right.left = None
root.right.right.right = None

bst = bst.BST()

bst.display(root)

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
