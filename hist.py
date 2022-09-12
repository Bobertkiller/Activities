import statistics
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy

df = pd.read_excel('tmpD3A8.xls')
my_list = df['PIB - preços de mercado (preços 2010) - R$ de 2010 (milhões)  - Instituto Brasileiro de Geografia e Estatística, Sistema de Contas Nacionais (IBGE/SCN Anual) - SCN10_PIBP10 - '].tolist()

desvio = statistics.pstdev(my_list)
print("O desvio padrão é (usando função pre programada): ", desvio)

var = desvio * desvio
print("A variância é (usando função pre programada): ", var)

maior = max(my_list)
menor = min(my_list)

amplitude = maior - menor
print("A amplitude é (usando função pre programada) : ", amplitude)


a = len(my_list)
b = sum(my_list)
media = b/a
print(f"A média é: ", media)

print(f"a mediana pre programada é: {statistics.median(my_list)}")

if((len(my_list) % 2) == 0):
    my_list.sort
    mediana1 = my_list[int(len(my_list) / 2)]
    mediana = my_list[int(len(my_list) / 2) - 1]
    mediana = mediana + mediana1
    mediana = mediana / 2
else:
    mediana = my_list[int(len(my_list) / 2)]
print("A mediana é: ", mediana)

x = 0
desvio = []
c = []
for x in range(len(my_list)):
    d = (my_list[x] - media)
    desvio.append(d)
    x = x + 1

for x in range(len(my_list)):
    desvio4 = desvio[x] ** 2
    c.append(desvio4)
    x = x + 1

somado = sum(c)

desvio_pop = somado / len(desvio)
calango = len(desvio) - 1
desvio_amo = somado / calango
print("A variação populacional é: ", desvio_pop)
print("A variação amostral é: ", desvio_amo)
desvio_final = math.sqrt(desvio_pop)
print("O desvio padrão populacional é: ", desvio_final)
desvio_amostra_end = math.sqrt(desvio_amo)
print("O desvio padrão amostral é: ", desvio_amostra_end)
desvioamostral = statistics.stdev(my_list)
print("O desvio padrão amostral é (usando função pre programada) : ", desvioamostral)

my_list.sort()

cv = (statistics.stdev(my_list) / len(my_list)) * 100
print(f'Coeficiente de Variação pre programada : {cv}%')

coef_pop = (desvio_pop / media) * 100
print(f"coeficiente de variação populacional é: {coef_pop}")

coef_amostra = (desvio_amo / media) * 100
print(f"coeficiente de variação amostral é: {coef_amostra}")


print(
    f'O Quantil pre programado é: {numpy.quantile(my_list, [0.25,0.5,0.75])}')

if((len(my_list) % 2) == 0) and (((len(my_list)/2) % 2) == 0):
    mediana1 = my_list[int(len(my_list) / 2)]
    mediana = my_list[int(len(my_list) / 2) - 1]
    mediana = mediana + mediana1

    mediana = mediana / 2

    quartil_1 = my_list[int(len(my_list) / 4)]
    quartil_p = my_list[int(len(my_list) / 4) - 1]
    quartil_1 = quartil_1 + quartil_p
    quartil_1 = quartil_1 / 2

    quartil_3 = my_list[int(len(my_list) * (3/4))]
    quartil_m = my_list[int(len(my_list) * (3/4)) - 1]
    quartil_3 = quartil_3 + quartil_m
    quartil_3 = quartil_3 / 2

    print(
        f"Primeiro Quartil: {quartil_1}, Segundo Quartil: {mediana}, Terceiro Quartil: {quartil_3}")
elif ((len(my_list) % 2) == 0) and (((len(my_list)/2) % 2) != 0):
    mediana1 = my_list[int(len(my_list) / 2)]
    mediana = my_list[int(len(my_list) / 2) - 1]
    mediana = mediana + mediana1
    mediana = mediana / 2

    quartil_1 = my_list[int(len(my_list) / 4)]

    quartil_3 = my_list[int(len(my_list) * (3 / 4))]

    print(
        f"Primeiro Quartil: {quartil_1}, Segundo Quartil: {mediana}, Terceiro Quartil: {quartil_3}")

else:
    mediana = my_list[int(len(my_list) / 2)]

    quartil_1 = my_list[int(len(my_list) / 4)]
    quartil_p = my_list[int(len(my_list) / 4) - 1]
    quartil_1 = quartil_1 + quartil_p
    quartil_1 = quartil_1 / 2

    quartil_3 = my_list[int(len(my_list) * (3 / 4))]
    quartil_m = my_list[int(len(my_list) * (3 / 4)) - 1]
    quartil_3 = quartil_3 + quartil_m
    quartil_3 = quartil_3 / 2
    print(
        f"Primeiro Quartil: {quartil_1}, Terceiro Quartil: {quartil_3}, Mediana: {mediana}")
plt.hist(my_list)
plt.show()
plt.boxplot(my_list)
plt.show()
