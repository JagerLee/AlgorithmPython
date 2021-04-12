def bubble_sort(alist):
    if not isinstance(alist,list):
        print("type error")
        return
    else:
        num = len(alist)
        for i in range(num-1):
            for j in range(num-1-i):
                if alist[j] > alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]

