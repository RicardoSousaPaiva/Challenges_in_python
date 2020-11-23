from random import shuffle
a1 =str(input('Aluno(a) 1: '))
a2 =str(input('Aluno(a) 2: '))
a3 =str(input('Aluno(a) 3: '))
a4 =str(input('Aluno(a) 4: '))
at =[a1,a2,a3,a4]
shuffle(at)
print('Ordem das apresentações é, respectivamente:\n',at)