# title Merge two lists
# description на входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив
#Элементы списка это целые числа
#O(n)
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