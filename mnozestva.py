tmp = set()
tmp2= {2, 3, 4, 3} # в множестве содержаться только уникальные элементы
tmp2.add(7) #добавить элемент
tmp2.discard(2) #удалить элемент
print(tmp2)
tmp2.clear() # очистить
print(tmp2)
print("-------------")
n = int(input())
used = set()
for i in range(n):
    promo = input()
    if promo in used:
        print("sorry")
    else:
        used.add(promo)
print(len(used))

print("-------------")

c1 = int(input())
cl1 = []
for i in range(c1):
    name = input()
    cl1.append(name)

# множество из списка
uc1 = set(cl1)


c2 = int(input())
cl2 = []
for i in range(c2):
    name = input()
    cl2.append(name)

uc2 = set(cl2)

print(uc1.union(uc2)) # объединение множеств

print(uc1.intersection(uc2)) # пересечение множеств
