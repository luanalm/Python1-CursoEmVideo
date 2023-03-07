x = int(input('De qual número deseja saber a tabuada? '))
print(' ')

for count in range(10):
    print('%d x %d = %d' % (x, count+1, x*(count+1)))
