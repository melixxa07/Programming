import numpy as np
a=np.arange(9)
print(a)

# -------------- #

# Importamos librerías
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


""" DEFINIMOS LOS INTERVALOS DE LA FUNCIÓN """
# Lista de valores para la variable independiente
# Definimos el paso:
p=0.001

# Intervalo: (se hace entre parentesis porque es un intervalo)
t1=np.arange(0,2,p)
t2=np.arange(2,4,p)
#t=t1+t2
t=t1
t_2=t2


# Se generan los valores de y (según su restricción en t)
y1=np.sin((np.pi)*t)*np.cos((np.pi)*t)

fn=list(y1)+list(y1)
tn=list(t1)+list(t2)

""" AÑADIMOS EL PERIODO """
# Modificamos T(periodo) lim_sup-lim_inf
T=2
w=(2*np.pi)/T

""" CREAMOS LA SERIE DE FOURIER """
    
# 1. Llamando la fn simbólica
# Definimos la función en términos de la variable (t)
# Escribimos la fn que se integraría
fs1= lambda t:(np.sin((np.pi)*t)*np.cos((np.pi)*t))*np.sin(i*t*w)
fc1= lambda t:(np.sin((np.pi)*t)*np.cos((np.pi)*t))*np.cos(i*t*w)
# fs:Función con sen(t) ; fc:Función con cos(t)
# La i es para reemplazar y operar con diferentes valores de n

# 2. Contador de la suma parcial
n=5
# Creamos una lista vacía para la sumatoria de an y bn
An=[]
Bn=[]


# Inicializamos la suma
sum=0
sum_0=0
for i in range(n+1):
# Realizamos la integral de 0 a 2
    an=quad(fc1,0,2)[0]*(1/(T/2)) 
    An.append(an)
   # print(An)

for i in range(n+1):
# Realizamos la integral de 0 a 2
    bn=quad(fs1,0,2)[0]*(1/(T/2))
    Bn.append(bn)

    
# "Definimos" la a_0 operandolo de esta manera pues el cos(0)=1 
# Y nos queda la integral/operación respectiva para a_0
for i in range(n+1):
    if i==0.0:
        sum=sum+An[i]/2

# Hacemos la sumatoria parcial de lo que está al lado del a_0
    else: 
        sum=sum+(An[i]*np.cos(i*t*w)+Bn[i]*np.sin(i*t*w))


        
# 3. Graficamos los valores
# Gráfica de la fn aproximada según el valor de n
plt.plot(t,sum,'b', label='n=5')
plt.plot(t_2,sum,'b')
#plt.plot(t,sum,'b')
# Grácica de la función real:
plt.plot(tn,fn,'r--', color='red', label='Función Real')      
plt.grid(True, linestyle='--', linewidth='0.5')
plt.legend(loc='lower left')
plt.title("Serie de Furier", fontname="Times New Roman")
plt.xlabel('t')
plt.ylabel('f(t)')
plt.show()