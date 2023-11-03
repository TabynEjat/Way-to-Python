def chet(a):
    if a % 2 == 0:
        return True
    return False

print(chet(5))
print(chet(4))
print("-------------")
def tmp(name):
    print(f'Hello, {name}')

tmp('Stas')
print("-------------")
def vis(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

y = int(input())
print(vis(y))
print("-------------")

def nechet(a):
    return (a % 2 != 0)

def res(l):
    for el in l:
        if(nechet(el)):
            print(el)

tmp = [1, 3, 2, 4, 5, 6]
res(tmp)
print("-------------")


def new_year():
    print("Happy New Year")

def birthday():
    print('name?')
    name = input()
    print(f'Happy Birthday, {name}!')

def march8():
    print("Happy 8th of March")

n = int(input())
for i in range(n):
    cm = input()
    if cm == 'NM':
        new_year()
    elif cm == 'HB':
        birthday(name)
    elif cm == 'M8':
        march8()
    else:
        print('non comand')
