bank= {'anton':10 , 'stas':20 ,'dima':4 } # клчи должны быть уникальными, если ключ повторяется то берется тот что стоит последним по индексу
print(bank['anton'])
bank['stas'] = 190
print(bank)
print(bank.keys()) # вывод ключей
print(bank.values())# вывод значений по ключам
print(bank.items())# выаод пар ключ значение
for k in bank.keys():
    print(k)

bank.pop('anton')
print(bank)

print("----------------")
newbank = dict()
zap = int(input())
for i in range(zap):
    req = input()
    if req == "c":
        k = input()
        newbank[k] = 0
       # print(newbank)
    elif req == "add":
        k = input()
        amount = int(input())
        if k in newbank.keys():
            newbank[k] += amount
        else: 
            print("sorry")
    else:  
         print("sorry2")
print(newbank)
    