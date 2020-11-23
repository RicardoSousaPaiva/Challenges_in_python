#n1 =int(input('Digite um número:' ))
#n2 =int(input('Digite outro número: '))
#print(f'A soma de {n1} e {n2} é {n1+n2}')

#m=int(input('Digite o valor em metros: '))
#mm = (m*1000)
#print(f'O valor de {m} metros equivale a {mm} milímetros.')

#d=int(input('Quantidades de dias: '))
#h=int(input('Quantidade de horas: '))
#m=int(input('Quantidade de minutos: '))
#s=int(input('Quantidade de segundos: '))
#ts=(d*60*60*60+h*60*60+m*60+s)
#print(f'{d} dias, {h} horas, {m} minutos e {s} segundos equivale a {ts} segundos.')

#s=float(input('Digite o valor do salário: '))
#pa=float(input('Digite a porcentagem de aumento: '))
#a=(s*pa/100)
#ns=(s+a)
#va=(ns-s)
#print(f'Você teve o aumento de R${va}. Com isso, o seu salário fica R${ns}.\nParabéns pelo aumento!')

#m=float(input('Difite o valor da mercadoria: '))
#pd=float(input('Digite o porcentagem de desconto: '))
#d=(m*pd/100)
#nv=(m-d)
#vd=(m-nv)
#print(f'Você teve R${vd:.2f} de desconto. A mercadoria fica no valor de R${nv}.\nVolte sempre!')

#d=int(input('Qual distãncia pecorrida em Km: '))
#v= int(input('QUal a velocidade em Km/h: '))
#t=(d/v)
#print(f'Numa distãncia de {d}Km a {v}Km/h o tempo de viagem será de {t:.2f} horas.')

#c=int(input('Temperatura em Celsius:'))
#f= 9*5/5+32
#print(f'O valor de {c} Celsius equivale a {f} Fahrenheit.')

#f=int(input("Temperatura em Fahrenheit: "))
#c= (f-32)*5/9
#print(f'O valor de {f} equivale a {c:.0f} celsius.')

#k=int(input('Quantidade de Km percorridos: '))
#d=int(input('Dias alugados: '))
#pg=(k*0.15 + d*60)
#print(f'Com {d} dias alugados e {k} Km pecorridos o valor do aluguel fica R$ {pg}.\nVOLTE SEMPRE!')

#c=int(input('Quantidade de cigarros fumados por dia: '))
#af=int(input('Quantidade de anos como fumante: '))
#tc=(af*365*c)
#dp= (tc/144)
#print(f'Você perdeu {dp:.0f} dias de vida.\n PARE DE FUMAR!')

#print(len(str(2**1000000)))

# =========================================== ATIVIDADE 2 =========================================================================================
#a=float(input('Lado 1: '))
#b=float(input('Lado 2: '))
#c=float(input('Lado 3: '))
#if a < b+c and b < c+a and c < a+b:
#    print('Estas medidas são de um triângulo', end='')
#    if a == b == c:
#        print(' Equilátero') 
#    elif a != b != c:
#        print(' Escaleno!')
#    else:
#        print(' Isóseles')
#else:
#    print('Estas medidas não fazem parte de um triângulo') 
#import urllib.request
#preço = 99.99
#while preço >= 4.74:
#    pagina = urllib.request.urlopen(
#    'http://beans.itcarlow.ie/prices-loyalty.html') 
#    texto = pagina.read().decode('utf8') 
#    onde = texto.find('>$')
#    inicio = onde + 2
#    fim = inicio + 4
#    preço = float(texto[inicio:fim])
#print (f'Comprar: R$ {preço:.2f}')
a=int(input('Digite o primeiro lado: '))
b=int(input('Digite o segundo lado: '))
c=int(input('Digite o terceiro lado: '))
if a < b+c and b < c+a and c < a+b:
    print(' As medidas formam um triângulo ', end='')
    if a == b == c:
        print('Equilátero!')
    elif a != b != c != a:
        print('Escaleno!')
    else:
        print('Isóscele!')
else:
    print('As medidas não formam um triângulo!') 