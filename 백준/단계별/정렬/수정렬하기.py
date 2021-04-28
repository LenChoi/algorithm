n = int(input())
result = list()

for i in range(n):
    result.append(int(input()))
result.sort()

for i in result:
    print(i)