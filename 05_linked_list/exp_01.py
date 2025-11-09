import random
import linked_list as LL

ll = LL.LinkedList()

random.seed(1)

# 10個のリストを生成し，先端ノードに挿入
rnbs = random.sample(range(15), 10)

print(rnbs)

for i in rnbs:
    ll.insert_head(i)

ll.display()
