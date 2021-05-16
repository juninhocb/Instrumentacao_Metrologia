import numpy as np  
import matplotlib.pyplot as plt
import quantize as qt

s_analog = 4.5 * np.load ('sample.npy') #importa o sinal análogico

n = 3 # número de bits
s_analog_midrise = qt.quantize(s_analog, n, 'midtread')
plt.plot(s_analog_midrise, label = 'sinal quantizado')
plt.plot (s_analog, label = 'sinal analógico')

plt.legend(loc='best')
plt.grid()
plt.xlabel('entrada')
plt.ylabel('saída')
plt.ylim(-1.3, 1.3)
plt.show()

