import numpy as np  
import quantize as qt
import matplotlib.pyplot as plt

s_analog = 4.5 * np.load ('sample.npy') #importa o sinal análogico

x = 0 #sinal de entrada
y = 0 #sinal de saída
xfinal = 0 #efeito somatório
yfinal = 0 #efeito somatório
xfinal2 = 0 #efeito somatório
yfinal2 = 0 #efeito somatório

lista_bits = [2, 3, 4, 5, 6, 7, 8] 

for n in lista_bits:
    s_analog_qnt = qt.quantize(s_analog, n, 'midtread')
    
    for t1 in range(0,100,1): #Considerando o número de amostras igual a 100
        y = np.square(s_analog_qnt)
        yfinal = yfinal + y  
     
    for t2 in range(0,100,1): #Considerando o número de amostras igual a 100
        x = np.square(s_analog)
        xfinal = xfinal + x 
        
    xfinal2 = np.sum(xfinal)/100 # potência media do sinal de entrada
    yfinal2 = np.sum(yfinal)/100 # potência media do sinal de saída
    z = abs(yfinal2 - xfinal2)  # potência media do erro (pois log não admite valores negativos)
    print("SNRdB do bit " + str(n) + " = " + str(10*np.log10(xfinal2/z)))

plt.plot (s_analog, label = 'sinal original')

plt.legend(loc='best')
plt.grid()
plt.xlabel('entrada')
plt.ylabel('saída')
plt.ylim(-1.3, 1.3)
plt.show()
            
        



