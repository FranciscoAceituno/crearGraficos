import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


class Histograma:

    df = any
    def __init__(self, dfInicial):
        self.df = dfInicial
    
    def createHistogram(self):
        dfGrafico = self.df.drop('zip_code', axis=1)
        dfGrafico = dfGrafico[dfGrafico['public_transportation_pct'] > 0]
        dfGraficoBajoUso = dfGrafico[dfGrafico['public_transportation_pct'] <= 10]
        dfGraficoAltoUso = dfGrafico[dfGrafico['public_transportation_pct'] > 10]
        pctVsPoblacionBajo = dfGraficoBajoUso.groupby('public_transportation_pct').sum().reset_index()
        pctVsPoblacionAlto = dfGraficoAltoUso.groupby('public_transportation_pct').sum().reset_index()

        # pctVsPoblacion.to_excel("salidaPCT.xlsx", index=0)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,8), sharex=True) # 1 fila, 2 columnas
       # Graficar el primer histograma en el primer subplot (ax1) con color azul
        ax1.hist(data = pctVsPoblacionBajo, x="public_transportation_pct", weights="public_transportation_population", alpha=0.5, color='blue',edgecolor='black', linewidth=1.2, label='Población con uso de 0 al 10 %')
        ax1.set_xlim(0, 50)
        ax1.xaxis.set_major_locator(plt.MultipleLocator(10)) 
        ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
        ax1.legend()

        # Graficar el segundo histograma en el segundo subplot (ax2) con color naranja
        ax2.hist(data= pctVsPoblacionAlto, x="public_transportation_pct", weights="public_transportation_population", alpha=0.5, color='red',edgecolor='black', linewidth=1.2, label='Población con uso sobre el 10 %')
        ax2.set_xlim(0, 100)
        ax2.xaxis.set_major_locator(plt.MultipleLocator(10)) 
        ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
        ax2.legend()

        fig.suptitle('Comparación de Histogramas', fontsize=14)

        # Ajustar el diseño de los subplots para evitar superposiciones
        plt.tight_layout()

        # Mostrar el gráfico
        plt.show()