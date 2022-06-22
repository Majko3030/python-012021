def least_larger(a, i):
    minimum_i = a[i]
    array_b = a[:]
    while min(array_b) <= minimum_i:
        array_b.remove(min(array_b))
        print(a)
    if array_b:
        return a.index(min(array_b))
    else:
        return -1

print(least_larger( [4, 1, 3, 5, 6], 0))