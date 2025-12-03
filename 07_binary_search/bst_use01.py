# レベルゼロ（ルート）
root = Node(40)

# レベル１
root.left = Node(30)
root.right = Node(70)

# レベル2
root.left.left = Node(10)
root.left.right = None
root.right.left = Node(60)
root.right.right = Node(90)

# レベル3
root.left.left.left = None
root.left.left.right = Node(20)
root.right.left.left = None
root.right.left.right = None
root.right.right.left = None
root.right.right.right = None

bst = BST()

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
