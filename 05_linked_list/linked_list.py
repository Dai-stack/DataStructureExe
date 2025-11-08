class Node:
    def __init__(self, key):
        self.key = key
        self.ref_next = None


class LinkedList:
    def __init__(self):
        self.head = None


node1 = Node(30)
node2 = Node(40)
node3 = Node(10)
node4 = Node(50)
node5 = Node(20)

# print(node1.key, node1.ref_next)

ll = LinkedList()

ll.head = node1

node1.ref_next = node2
node2.ref_next = node3
node3.ref_next = node4
node4.ref_next = node5

# インスタンスnode1のkeyにアクセス
print(ll.head.key, end=" ")

# インスタンスnode1のref_next(node2)のkeyにアクセス
print(ll.head.ref_next.key, end=" ")

print(ll.head.ref_next.ref_next.key, end=" ")
print(ll.head.ref_next.ref_next.key, end=" ")
print(ll.head.ref_next.ref_next.ref_next.key, end=" ")
print(ll.head.ref_next.ref_next.ref_next.ref_next.key, end=" ")
# print(ll.head.ref_next.ref_next.ref_next.ref_next.ref_next.key, end=" ")
