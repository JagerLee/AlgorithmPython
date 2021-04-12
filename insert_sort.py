def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        j = i-1
        temp = alist[i]
        while j >= 0 and temp < alist[j]:
            alist[j], alist[j+1] = temp, alist[j]
            j -= 1


alist = [79,561,1,56,33,88,9884,12,95,33]

insert_sort(alist)
print(alist)
