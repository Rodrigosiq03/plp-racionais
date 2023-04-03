from racional import Racional


num1_racional = Racional(2, 5)
num2_racional = Racional(3, 4)
result_razao = num1_racional.razao()
result_soma = num1_racional.sum(num2_racional)
result_sub = num1_racional.sub(num2_racional)
result_mult = num1_racional.mult(num2_racional)
print(f"O resultado da razao do racional 1 é {result_razao}")
print(f"O resultado da soma do racional 1 é {result_soma}")
print(f"O resultado da subtração do racional 1 é {result_sub}")
print(f"O resultado da multiplicação do racional 1 é {result_mult}")



