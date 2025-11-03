import random


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        # mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return None


random.seed(1)

N = 10
B = 20

M = 5

rnbs = random.sample(range(B, B + N), N)

# ソート処理
rnbs.sort()

print("ランダム配列：", rnbs)

# 探索実施
print(f"binary_search: -> {binary_search(rnbs, 25)} \n ")


# 配列の範囲よりMだけ上下を拡大
for i in range(B - M, B + N + M):
    print(f"binary_search:{i} -> index:{binary_search(rnbs, i)}")
