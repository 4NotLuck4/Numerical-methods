import math

a = int(input('Введите нижнюю границу: '))
b = int(input('Введите верхнюю границу: '))

n = int(input('Введите количество итераций: '))

h = (b - a) / n
i = 0
sum_minus = 0
sum_plus = 0

while i < n:
    xi = a + h * i

    xi_minus = xi + h / 2 - h / (2 * math.sqrt(3))

    xi_plus = xi + h / 2 + h / (2 * math.sqrt(3))

    print(f"{i}: yi_minus = {0.37 * math.exp(xi_minus)} yi_plus = {0.37 * math.exp(xi_plus)}")

    sum_minus += 0.37 * math.exp(xi_minus)
    sum_plus += 0.37 * math.exp(xi_plus)
    i += 1

print(f"Сумма yi-: {sum_minus}")
print(f"Сумма yi+: {sum_plus}")

sum = sum_minus + sum_plus
print(f"Сумма: {sum}")

result = sum * (h / 2)
print(f"Результат равен: {round(result, 8)}")