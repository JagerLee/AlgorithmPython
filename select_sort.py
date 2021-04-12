
def select_sort(alist):
    n = len(alist)
    temp = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if alist[j] < alist[temp]:
                temp = j
        alist[i], alist[temp] = alist[temp], alist[i]


alist = [79,561,1,56,33,88,9884,12,95,33]

select_sort(alist)
print(alist)