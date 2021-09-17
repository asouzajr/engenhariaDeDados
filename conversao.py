# Conversão de um tipo de dado inteiro para ponto flutuante
# Observe que não é um arrendodamento, apenas consideração da parte inteira do número
a = 9
b = 3.14
c = 3.66
d = 3.5
print("O resultado é: ", float(a))
print('O resultado é: ', int(b))
print('O resultado é: ', int(c))
print('O resultado é: ', int(d))

# Com base hexadecimal e binária
e = 200
f = 500
print('200 em hexadecimal é: ', hex(e))
print('500 em hexadecimal é: ', bin(e))

# Funções abs e round

# Para retornar o valor absoluto
g = -8
print('O valor absoluto de -8 é: ', abs(g))

# Função para arrendodamento
h = 3.436
i = 3.435
j = 3.434

print('O valor após arrendodamento da variável h é: ', round(h, 2))
print('O valor após arrendodamento da variável i é: ', round(i, 2))
print('O valor após arrendodamento da variável j é: ', round(j, 2))