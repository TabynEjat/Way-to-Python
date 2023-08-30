a = int(input())
cnt = 0
while a >=0:
    a -= 2
    cnt +=1
    print(a, cnt)

print("-------------")

clients, cola = map(int, input().split())
cnt = 0

while (clients > 0) and (cola >= 0):
    cans = int(input())
    clients -= 1
    if cola >= cans:
        cnt +=1
        cola -= cans

print(cnt)

print("-------------")


a, b = map(int, input().split())
for i in range(b, a - 1, -1):
    print(i)

print("-------------")

n = int(input())
for i in range(n):
    salary = int(input())
    if salary % 2 == 0:
        print(i + 1, "fired")
    else:
        print(i + 1, "good")