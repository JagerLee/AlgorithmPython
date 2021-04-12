import numpy as np


def quick_sort(alist):
    if len(alist) > 1:
        l, r = [], []
        mid = alist[-1]
        alist.pop()
        for i in alist:
            if i <= mid:
                l.append(i)
            else:
                r.append(i)
        quick_sort(l)
        quick_sort(r)
        alist.clear()
        for i in l + [mid] + r:
            alist.append(i)


if __name__ == "__main__":
    alist = np.arange(1, 1000001)
    np.random.shuffle(alist)
    alist = alist.tolist()
    quick_sort(alist)

