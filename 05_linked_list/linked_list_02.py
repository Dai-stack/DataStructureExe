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
        # Headのリンクを新しいノードに
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
