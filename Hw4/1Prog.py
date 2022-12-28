#from decimal import Decimal, getcontext
#getcontext().prec = 5
#number = Decimal('9')
#print(number.quantize(Decimal('0.0001')))


chisl = int(input('Введите число: '))
from decimal import Decimal, getcontext
getcontext().prec = 5
number = Decimal(chisl)
print(number.quantize(Decimal('0.0001')))

