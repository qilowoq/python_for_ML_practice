# title Squared sorted
# description Дан отсортированный список в неубавющем порядке. Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке
# Элементы списка это целые числа
# O(n)
#---end---

def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def squares(l):
    ind = len(l) - 1
    for i in range(len(l)):
        if l[i] >= 0:
            ind = i
            break
    a = []
    b = []
    for i in range(ind, len(l)):
        a.append(l[i]**2)
    for j in range(ind-1, -1, -1):
        b.append(l[j]**2)
    return merge(a, b)