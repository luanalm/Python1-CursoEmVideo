
# Exemplo: \033[0;33;44m

# Estilos/Style (Ocupando o lugar do 0 no comando acima)
# 0 - Nenhum/None
# 1 - Negrito/Bold
# 4 - Sublinhado/Underline
# 7 - Inverter as cores/Negative

# Texto/Text (Ocupando o lugar do 33 no comando acima)
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Magenta
# 36 - Ciano
# 37 - Cinza

# Fundo/Back (Ocupando o lugar do 44 no comando acima)
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Magenta
# 46 - Ciano
# 47 - Cinza

# teste1 = \033[0;30;41m
# teste2 = \033[4;33;44m
# teste3 = \033[1;35;43m
# teste4 = \033[30;42m
# teste5 = \033[m
# teste6 = \033[7;30m

print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;45mOlá, Mundo!\033[m')

nome = str(input('Nome: '))
print('Olá, {}{}{}! Muito prazer em te conhecer!'.format('\033[4;41m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'ciano':'\033[4;46m',
         'b&w':'\033[7m'}

print('Olá, {}{}{}! Muito prazer em te conhecer!'.format(cores['b&w'], nome, cores['limpa']))
