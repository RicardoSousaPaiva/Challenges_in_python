from math import sin, cos, tan, radians
a = float(input('Digíte o ângulo: '))
seno= sin(radians(a))
coseno= cos(radians(a))
tagente= tan(radians(a))
print(f' O ângulo {a:.0f} tem \n*SENO {seno:.2f} \n*COSSENO {coseno:.2f} \n*TANGENTE {tagente:.2f}') 
