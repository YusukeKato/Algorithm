# クイックソート（再帰あり）
# 実行時間 : 平均 O(n log n) : 最悪 O(n^2)
# 安定ではない
def quicksort(a, first, last):
    x = a[int((first + last) / 2)]
    i = first
    j = last
    while True:
        while a[i] < x:
            i += 1
        while x < a[j]:
            j -= 1
        if i >= j:
            break
        t = a[j]
        a[j] = a[i]
        a[i] = t
        i += 1
        j -= 1
    if first < i - 1:
        quicksort(a, first, i - 1)
    if j + 1 < last:
        quicksort(a, j + 1, last)

a = [6,4,3,4,8,2]
quicksort(a, 0, len(a) - 1)
print(a)
