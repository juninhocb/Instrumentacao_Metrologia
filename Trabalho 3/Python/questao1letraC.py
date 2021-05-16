import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/eduar/Desktop/jr/Instrumentação e Metrologia/Trabalho 3/Python/questaoB_T3.txt', sep = '\t')
'''
for col in data.columns:
    print(col)
'''
tensao = data['V(vout+)-V(vout-)']

plt.figure(figsize=(8, 6))
plt.hist(tensao, bins=10)
plt.title('Distribuição de Tensões')
plt.xlabel('Tensão (Volts)')
plt.ylabel('Quantidade')

plt.show()


