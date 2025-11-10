import time
import random
import linked_list as LL

ll = LL.LinkedList()

random.seed(1)

N = 10000
rnbs = random.sample(range(N), N)

# 先頭への挿入
ts_start = time.time()
for i in rnbs:
    ll.insert_head(i)

ts_end = time.time()

print(f"InsertHead:{ts_end - ts_start}")

# 末尾への挿入
ts_start = time.time()
for i in rnbs:
    ll.isnert_tail(i)

ts_end = time.time()

print(f"InsertTail:{ts_end - ts_start}")
