def rotate(l, n):
    return l[n:] + l[:n]

l=[1,2,3,4]
print(rotate(l,2))