# Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex: Digite um numero: 1834
# unidades: 4 dezena: 3 centena: 8 milhar: 1

num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero {}'.format(num))
print('Unidades {}'.format(u))
print('Dezenas {}'.format(d))
print('Centenas {}'.format(c))
print('Milhar {}'.format(m))