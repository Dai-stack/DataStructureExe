class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 行きがけ順走査
    def preorder(self, node):
        if node is None:
            return
        print(node.key, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    # 通りがけ順走査
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.key, end=" ")
        self.inorder(node.right)

    # 帰りがけ順走査
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key, end=" ")

    # BSTを表示する①
    def display(self, node, levels=0):
        if node is None:
            return

        self.display(node.right, levels + 1)
        print("----" * 4 * levels + str(node.key))
        self.display(node.left, levels + 1)

    # BSTを表示する②
    def display_r(self, node, levels=0):
        if node is None:
            return

        self.display(node.left, levels + 1)
        print("----" * 4 * levels + str(node.key))
        self.display(node.right, levels + 1)

    # 最小ノードを探索
    def find_min_node(self, node):
        while node.left:
            node = node.left
        return node.key

    # 最大ノードを探索
    def find_max_node(self, node):
        while node.right:
            node = node.right
        return node.key

    # ノード数を数える
    def find_tree_size(self, node):
        count = 0
        if node is None:
            return
        self.find_tree_size(node.left)
        self.find_tree_size(node.right)
        return count


if __name__ == "__main__":
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
