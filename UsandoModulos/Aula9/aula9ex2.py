# Exercício 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Por exemplo: 1834. unidade 4, dezena 3, centena 8, milhar 1

while(True): 
	num = int(input("Escolha um número entre 0 e 9999: ")) 
	if num not in range(0,10000): 
		print('O número escolhido é inválido') 
	else:
         if num < 10:
            num = str(num) # Transforma a var num de Int para String para poder usar o Fatiamento
            print('O número {} tem {} unidades.'.format(num, num[0])) # 
         elif (num >= 10) and (num < 100):
            num = str(num)
            print('O número {} tem {} dezenas e {} unidades.'.format(num, num[0], num[1]))
         elif (num >= 100) and (num < 1000):
            num = str(num)
            print('O número {} tem {} centenas, {} dezenas e {} unidade.'.format(num, num[0], num[1], num[2]))
         else:
            num = str(num)
            print('O número {} tem {} milhares, {} centenas, {} dezenas e {} unidades.'.format(num, num[0], num[1], num[2], num[3]))
         break

# Com certeza tem uma forma otimizada de fazer esse exercício, mas pelo menos consegui deixar ele funcional :D
# Lembretes: focar em aprender otimização e reescrever a resolução do professor para lembrar o método usado

# RESOLUÇÃO DO PROFESSOR
# num = int(input('Escolha um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('O número {} tem {} milhares, {} centenas, {} dezenas e {} unidades.'.format(num, m, c, d, u))
