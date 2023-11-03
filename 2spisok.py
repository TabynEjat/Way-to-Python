

tmp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(tmp[1][0])
print(tmp)
for i in tmp:
    print(*i)
print('----------')

def printlist(t):
    for i in t:
        print(*i)

n = int(input())
tmp = []
for i in range(n): 
    a = list(map(int,input().split()))
    tmp.append(a)
printlist(tmp)
print('----------')

def printlist(t):
    for i in t:
        print(*i)


tmp = [[1 for i in range(7)] for i in range(5)]
printlist(tmp)
print('----------')

x = int(input())
y = int(input())
house = [[0 for i in range(y)] for i in range(x)]
cnt = 1
for i in range(-1, -x - 1, -1):
    if i % 2 == 1:
        for j in range(y):
            house[i][j] = cnt
            cnt += 1
    else:
        for j in range(-1, -y - 1, -1):
            house[i][j] = cnt
            cnt += 1

printlist(house)

   











