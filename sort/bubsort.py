# バブルソート
# 実行時間 O(n^2)
def bubsort(a):
    k = len(a) - 1
    while k >= 0:
        j = -1
        for i in range(1, k+1):
            if a[i-1] > a[i]:
                j = i - 1
                x = a[j]
                a[j] = a[i]
                a[i] = x
        k = j

a = [2,6,9,1,4]
bubsort(a)
print(a)
