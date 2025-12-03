# BSTクラスを定義
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """insert a key into a bst"""
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            parent = None
            while True:
                parent = curr
                if node.key < parent.key:
                    curr = curr.left
                    if curr is None:
                        parent.left = node
                        return
                else:
                    curr = curr.right
                    if curr is None:
                        parent.right = node
                        return

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

    # ノード数
    def find_tree_size(self, node):
        s_left = 0
        s_right = 0
        if node.left is not None:
            s_left = self.find_tree_size(node.left)
        if node.right is not None:
            s_right = self.find_tree_size(node.right)
        return s_left + s_right + 1

    # ツリーの高さ
    def find_height(self, node):
        h_left = 0
        h_right = 0
        if node.left is not None:
            h_left = self.find_height(node.left)
        if node.right is not None:
            h_right = self.find_height(node.right)
        if h_left > h_right:
            return h_left + 1
        return h_right + 1

    # 探索
    # 見つかる場合:探索キーを返す
    # 見つからない場合:Noneを返す
    def search(self, key):
        curr = self.root
        while True:
            if curr is None:
                return None
            if curr.key is key:
                return key
            if curr.key > key:
                curr = curr.left
            else:
                curr = curr.right

    # 親ノードを返す
    def find_parent_node(self, key):
        parent = None
        curr = self.root

        if curr is None:
            return (parent, None)
        while True:
            if curr.key == key:
                return parent, curr
            if curr.key > key:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        return parent, curr

    # 子ノードの数を数える
    def count_child_node(self, node):
        n_child_node = 0

        if node.left and node.right:
            n_child_node = 2
        elif (node.left is None) and (node.right is None):
            n_child_node = 0
        else:
            n_child_node = 1
        return n_child_node

    # 削除（呼び出し用）
    def delete(self, key):
        """delete a key from a bst"""
        parent, node = self.find_parent_node(key)

        if parent is None and node is None:
            return None

        n_child_node = self.count_child_node(node)
        if n_child_node == 0:
            self.delete_node_0(parent, node)
        elif n_child_node == 1:
            self.delete_node_1(parent, node)
        else:
            self.delete_node_2(node)
        return None

    # 削除（子ノードが無いノードを削除する）
    def delete_node_0(self, parent, node):
        """n_child_node == 0"""
        if parent:
            if parent.right is node:
                parent.right = None
            else:
                parent.left = None
        else:
            self.root = None

    # 削除（子ノードが1つであるノードを削除する）
    def delete_node_1(self, parent, node):
        """n_child_node == 1"""
        next_node = None
        if node.left:
            next_node = node.left
        else:
            next_node = node.right

        if parent:
            if parent.left is node:
                parent.left = next_node
            else:
                parent.right = next_node
        else:
            self.root = next_node

    # 削除（子ノードが2つであるノードを削除する）
    def delete_node_2(self, node):
        """n_child_node == 2"""
        parent_lm_node = node
        lm_node = node.right
        while lm_node.left:
            parent_lm_node = lm_node
            lm_node = lm_node.left

        node.key = lm_node.key

        if parent_lm_node.left == lm_node:
            parent_lm_node.left = lm_node.right
        else:
            parent_lm_node.right = lm_node.right
