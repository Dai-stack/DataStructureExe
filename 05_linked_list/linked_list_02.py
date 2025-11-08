class Node:
    def __init__(self, key):
        self.key = key
        self.ref_next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ノードの値(key)をすべて表示する
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.ref_next
        print("")

    # 先頭へのノード挿入
    def insert_head(self, key):
        node = Node(key)
        # 新ノードのリンクはこれまで先頭にあったノードへリンクさせる
        node.ref_next = self.head
        self.head = node

    # 末尾へのノード挿入
    def isnert_tail(self, key):
        node = Node(key)

        # リストが空の場合
        if self.head is None:
            self.head = node
            return

        # リストが空でない場合
        last = self.head

        # 先頭からノードをたどっていき，新規ノードを末尾に挿入する
        while last.ref_next is not None:
            last = last.ref_next

        last.ref_next = node

    # 中間へのノード挿入
    def insert_mid(self, pos, key):
        index = 0
        curr = self.head

        while index < (pos - 1) and curr is not None:
            index += 1
            curr = curr.ref_next

        if pos == 0:
            new_node = Node(key)
            new_node.ref_next = curr
            self.head = new_node

        else:
            new_node = Node(key)
            new_node.ref_next = curr.ref_next
            curr.ref_next = new_node

    # 先頭ノード削除
    def delete_head(self):
        if self.head is None:
            print("This LinkedList is empty")

        node = self.head
        self.head = self.head.ref_next
        print("削除した先頭ノードのキー: ", node.key)
        return node.key

    # 末尾ノード削除
    def delete_tail(self):
        if self.head is None:
            print("This LinkedList is empty")
            return None

        curr = self.head
        prev = None

        # 最後尾のノードまでたどり，その参照をきる
        while curr.ref_next is not None:
            prev = curr
            curr = curr.ref_next
        prev.ref_next = None
        print("削除した最後尾ノードのキー: ", curr.key)
        return curr.key

    # 中間ノードの削除
    def delete_mid(self, pos):
        if self.head is None:
            print("This LinkedList is empty")
            return None

        curr = self.head
        prev = None
        index = 0

        while curr.ref_next is not None and index < pos:
            prev = curr
            curr = curr.ref_next
            index += 1

        if curr == self.head:
            self.head = curr.ref_next
            mid_key = curr.key

        else:
            prev.ref_next = curr.ref_next
            mid_key = curr.key

        print(f"削除した中間ノードのポジション: {pos}, キー: {curr.key}")
        return curr.key


node1 = Node(30)
node2 = Node(40)
node3 = Node(10)
node4 = Node(50)
node5 = Node(20)
ll = LinkedList()
ll.head = node1
node1.ref_next = node2
node2.ref_next = node3
node3.ref_next = node4
node4.ref_next = node5

ll.display()

ll.insert_head(90)

ll.display()

ll.isnert_tail(60)

ll.display()

ll.insert_mid(3, 55)

ll.display()

ll.delete_head()

ll.display()

ll.delete_tail()

ll.display()

ll.delete_mid(3)

ll.display()
