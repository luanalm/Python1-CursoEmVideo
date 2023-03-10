# Manipulando Cadeias de Texto

# FATIAMENTO

# C u r s o   e m   V í  d  e  o ' ' P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# Os espaços contam como um caracter também e o primeiro caracter conta como o caracter 0 e não como caracter 1.
# Sempre que há alguma alteração no comprimento da String (com transformação, divisão, etc.), a contagem de caracteres se altera de acordo com a mudança feita.

frase = 'Curso em Vídeo Python'

frase[9]        # apenas o caracter na casa 9, no caso 'V'
frase[9:13]     # os caracteres da casa 9 a casa 13, mas sem o da casa 13. Resposta: 'Víde'
frase[9:21]     # não dará nenhum erro, mas não é a melhor forma de fatiar
frase[9:21:2]   # o 2 faz ser registrado apenas de duas em duas casas. Resposta: 'VdoPto'
frase[:5]       # começa no caracter 0 e termina no caracter 5. Resposta: 'Curso', sem o espaço
frase[15:]      # começa no caracter anotado, no caso 15, e vai até o final da frase salva. Resposta: 'Python'
frase[9::3]     # começa no 9, vai até o fim da frase, pulando de três em três casas de caracteres. Resposta: 'VePh'


# ANÁLISE

len(frase)              # Mostra o comprimento da frase, nesse caso, 21 caracteres.
frase.count('o')        # Mostra o número de vezes que aparece a letra 'o'. R: 3
frase.count('o',0,13)   # Contagem com fatiamento, do caracter 0 ao 12, sem contar o caracter na posição 13. Resposta: 1
frase.find('deo')       # Mostra a posição que começa 'deo'. Resposta: 11
frase.find('Android')   # Não há 'Android' na frase. Resposta: -1
'Curso' in frase        # Para perguntar se existe, boolean. Resposta: True


# TRANSFORMAÇÃO - Não ocorre de forma definitiva
# Para ocorrer de forma definitiva é necessário usar 'frase = frase.replace()'

frase.replace('Python', 'Android')   # Troca uma parte da frase. Ficando: 'Curso em Vídeo Android'
frase.upper()   # Todas as letras que forem minúsculas ficam maiúsculas. 'CURSO EM VIDEO PYTHON'
frase.lower()   # Todas as letras em maiúsculo ficam em minúsculo. 'curso em vídeo python'
frase.capitalize()   # Primeira letra da frase maiúscula e o resto minúsculo. 'Curso em vídeo python'
frase.title()   # Tranforma todas as primeiras letras das palavras em maiúsculo e o resto em minúsculo. 'Curso Em Vídeo Python'

frase2 = '   Aprenda Python  '

frase2.strip()   # Remove os espaços do começo e fim da String. 'Aprenda Python'
frase2.rstrip()  # Remove somente os espaços do fim da String, lado direiro. '   Aprenda Python'
frase2.lstrip()  # Remove somento os espaços do começo da String, lado esquerdo. 'Aprenda Python  '


# DIVISÃO

frase.split()       # Divide a frase onde tem espaços, a transformando em uma lista. ['Curso', 'em','Vídeo', 'Python']
'-'.join(frase)     # Junta todos os elementos de frase com o elemento '-'. 'Curso-em-Vídeo-Python'
