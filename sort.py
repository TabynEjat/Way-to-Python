print('пузырик')
a = [4,9,0,6,7,23,17] 
n = len(a)
for i in range(n):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(*a)

print('фаст ')
a.sort() 
print(*a)

print("-------------")
def cmp(x):
    return x % 10

a.sort(key=cmp)
print(*a)
print("-------------")
sotr = 5
sph = [ 19, 38, 97, 5, 9]
hs = [ 10, 120, 4, 8 ,9]
res = []
for i in range(sotr):
    r = sph[i] * hs[i]
    res.append(r)
res.sort()
print(*res)
print("-------------")
def cmp(x):
    return( x // 10) + (x % 10)

tmp = [10, 45, 56, 40, 19, 46, 87, 68]

tmp.sort(key=cmp)
print(*tmp)
print("-------------")

a = 5
b = 1
c = 8
d = -19
print(max(a, b, c, d)) # можно и с min, работает со списками
print("Кортеж") #неизменяемый список
a = (2, 4, 9)
b = tuple() # zero
# но для него работают все теже методы что и для списков, что не меняют значений
poets =[ ('Pushkin',1203, 1209)( 'Chexov',1999, 1209) ( 'Blok', 1207, 1212)]
