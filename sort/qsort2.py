# クイックソート（再帰なし）
# 実行時間 平均 : O(nlogn) 最悪 : O(n^2)
# 安定ではない
import inssort as ins
def quicksort2(a):
    HOLD = 3  # 重要
    SIZE = 32
    left = 0
    right = len(a) - 1
    leftstack = []
    rightstack = []
    p = 0
    x = 0
    t = 0
    while True:
        if right - left <= HOLD:
            if p == 0: break
            p -= 1
            left = leftstack[p]
            right = rightstack[p]
        x = a[int((left+right)/2)]
        i = left
        j = right
        while True:
            while a[i] < x: i += 1
            while x < a[j]: j -= 1
            if i >= j: break
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1
        if i - left > right - j:
            if i - left > HOLD:
                leftstack.insert(p, left)
                rightstack.insert(p, i - 1)
                p += 1
            left = j + 1
        else:
            if right - j > HOLD:
                leftstack.insert(p, j + 1)
                rightstack.insert(p, right)
                p += 1
            right = i - 1
    ins.inssort(a)  # ある程度ソートしたら、挿入ソートに渡す

a = [2, 7, 5, 1, 4]
quicksort2(a)
print(a)
