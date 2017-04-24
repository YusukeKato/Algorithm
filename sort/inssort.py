# 挿入ソート
# 実行時間 : O(n^2)
# 安定である
def inssort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x

a = [4,6,2,1,8,5]
inssort(a)
print(a)
