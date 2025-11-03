import random


def linear_search(arr, key):
    l = len(arr)
    for i in range(l):
        if arr[i] == key:  # 添字の頭から順にアクセスしているだけ
            return i
    return None


random.seed(1)

N = 10
B = 50

rnbs = random.sample(range(B, B + N), N)

print("ランダム配列：", rnbs)

# 探索実施
print(f"linear_search:50 -> {linear_search(rnbs, 50)} \n ")


M = 5

# 探索範囲：45 - 65 配列の範囲よりMだけ上下を拡大
for i in range(B - M, B + N + M):
    print(f"linear_search:{i} -> index:{linear_search(rnbs, i)}")
