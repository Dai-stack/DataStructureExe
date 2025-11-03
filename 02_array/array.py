# arrayモジュールを使って配列を実装
import array

array = array.array("i", [10, 20, 30, 40])

for i in array:
    print(i, end=" ")

print()

# 要素の削除
del array[0]
print(array)


# 要素があるかどうか
print(10 in array)
