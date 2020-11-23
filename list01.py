from random import shuffle
a1 =str(input('Aluno(a) 1: '))
a2 =str(input('Aluno(a) 2: '))
a3 =str(input('Aluno(a) 3: '))
a4 =str(input('Aluno(a) 4: '))
at =[a1,a2]
at1=[a3,a4]
shuffle(at)
shuffle(at1)
print('A ordem das apresentações é como primeiro e segundo, respectivamente:', at, at1)






