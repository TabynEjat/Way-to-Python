tmp = 'abcdef'
print(tmp[0]) #  можно использовать отрицательную индексацию (-1) для вывода с конца строки
print(len(tmp)) # длина строки
print("-------------")

s1 = 'fgfdfgdhfghfjgfhfj'
print(s1[0:5:2]) #срез c шагом 2. млжно указать отрицательный шаг, тогда будет идти с последнего указанного элемента
print("-------------")

tmp = [4,3,2,1,0]
print(tmp[::2])
print("-------------")


tmp = '3 + 8 + 9 + 10'
t = tmp.split(' + ')
print(t)
print("-------------")

tmp = ['3','4','5','157']
print(' + '.join(tmp))
print("-------------")

name = input()
(print(f'Hello, {name}'))
print("-------------")

s1 = 'abc'
print(s1.upper()) # lower приводит к нижнему регистру
print("-------------")

print(ord('a')) # по таблице ASCII
print(chr(97))
print("-------------")
print("Шифр Цезаря")
t = "abzr"
for c in t:
    code = ord(c) + 3
    if code > 122:
        print(chr(97 + code - 122), end='')
    else:
         print(chr(code), end='')

