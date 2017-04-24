# 選択ソート（単純選択法）
# 実行時間　O(n^2)
# 安定である
def selectsort(a):
    for i in range(len(a)-1):
        min = a[i]
        k = i
        for j in range(i+1,len(a)):
            if a[j] < min:
                min = a[j]
                k = j
        a[k] = a[i]
        a[i] = min

a = [3,7,5,1,9,3]
selectsort(a)
print(a)
