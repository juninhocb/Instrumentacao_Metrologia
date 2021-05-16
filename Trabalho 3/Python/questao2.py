import pandas as pd

data = pd.read_csv('C:/Users/eduar/Desktop/jr/Instrumentação e Metrologia/Trabalho 3/Python/tensao_pt100.csv', sep = ',')

media = data['V0 (V)'].mean()

print('media:', media)

sigma = data['V0 (V)'].std()

print('desvio padrão: ', sigma)


