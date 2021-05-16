import pandas as pd
data = pd.read_csv('C:/Users/eduar/Desktop/jr/Instrumentação e Metrologia/Trabalho 3/Python/questaoB_T3.txt', sep = '\t')
incertezaMax = 0.192
incertezaMin = -0.172
soma = 0

rangeCalc = data['V(vout+)-V(vout-)'].between(incertezaMin, incertezaMax)

for i in rangeCalc:
    if (i):
        soma = soma + 1

print("Número de dados que aparecem dentro da incerteza calculada:", soma)
print("Resultado percentual: %", (soma/1500)*100)