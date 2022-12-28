#from decimal import Decimal, getcontext
#getcontext().prec = 5
#number = Decimal('9')
#print(number.quantize(Decimal('0.0001')))


chisl = int(input('Введите число: '))
#from decimal import Decimal, getcontext
#getcontext().prec = 5
#number = Decimal(chisl)
#print(number.quantize(Decimal('0.0001')))

#from math import chisl

d = int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(chisl, d)}')
