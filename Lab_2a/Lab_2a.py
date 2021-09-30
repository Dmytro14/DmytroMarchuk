A = 15
B = 76.7

print("Перша константа", False)
print("Друга константа", A)
print("Третя константа", B)

########

print(abs(-3.5), f"є рівним {abs(3.5)}")
print("Тип другої константи",type(A), "Тип третьої константи",type(B))

########

if B > 20:
    print("B > 20")
else:
    print("B < 20")

for i in range(3):
    print(i)

########

try:
    print("A Помножити на 2 =", A*2)
except Exception as e:
    print(e)
finally:
    print("Ось така у нас відповідь")

#####

with open("README.md", "r") as f:
    for line in f:
        print(line)

#####

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:   ", this_is_lambda('Дмитро', 'Марчук'))