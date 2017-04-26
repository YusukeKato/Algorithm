# ヒープソート
# 実行時間 : O(n log n)
# 安定ではない
# 基本、添え字は１から（０にー１を入れる）
def heapsort(n, a):
    i = 0; j = 0; k = 0; x = 0
    for k in range(int(n/2), 0, -1):
        i = k; x = a[i]
        while 2*i <= n:
            j = 2 * i
            if j < n and a[j] < a[j+1]: j += 1
            if x >= a[j]: break
            a[i] = a[j]; i = j
        a[i] = x
    while n > 1:
        x = a[n]; a[n] = a[1]; n -= 1; i = 1
        while 2*i <= n:
            j = 2 * i
            if j < n and a[j] < a[j+1]: j += 1
            if x >= a[j]: break
            a[i] = a[j]; i = j
        a[i] = x

a = [-1,5,4,7,1,6]
heapsort(len(a)-1, a)
print(a)
