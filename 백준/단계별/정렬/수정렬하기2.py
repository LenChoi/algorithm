def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

n = int(input())
result = list()

for i in range(n):
    result.append(int(input()))

merge_sort(result)
result.reverse()

for i in result:
    print(i)