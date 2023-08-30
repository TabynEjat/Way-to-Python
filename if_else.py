a, b = map(int, input().split())

if a < b:
    print("yes")
elif a == b:
    print("null")
else:
    print("no")

print("-------------")

cash, cost, cassa = map(int, input().split())

if cash >= cost and (cash - cost) <= cassa:  # для команды или используется ot
    print("cola")
else:
    print("water")
print("-------------")