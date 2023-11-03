arr = [3, 4, 9 ,1, 9]
print(arr)
print(*arr)
print(arr[2]) #отрицательная индексация позволяет обращаться с конца списка
arr[1] = 99
print(arr[1])
arr.append(199) #добавить в конец 
print(arr[-1])
print(len(arr))
arr.insert(3, 999) # добавить на позицию 3 число 999
arr.pop() # удалить элемент по умолчанию последний, если передать индекс удалит по нему
arr.reverse()
print(*arr)
print(arr.count(9))
arr.clear() # очистить список
print(*arr)
print("-------------")
n = int(input())
res = []
for i in range(n):
    arr = int(input())
    res.append(arr)
print(res)
print("-------------")
arr1 = list(map(int, input().split()))
print(arr1)
print("-------------")
n = int(input())
tmp = list(map(int, input().split()))
res = []
for i in range(len(tmp)):
    if tmp[i] != 50:
        res.append(tmp[i])
print(res)

print("-------------")
tmp = [1, 11, 111, 1111, 11111]
for i in tmp:
    print(i)
print("-------------")
arr = [3 for i in range(10)]
print(arr)
print(len(arr))
print("-------------")

