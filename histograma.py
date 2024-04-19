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
        dfGrafico = dfGrafico[dfGrafico['public_transportation_pct'] > 10]
        pctVsPoblacion = dfGrafico.groupby('public_transportation_pct').sum().reset_index()

        # pctVsPoblacion.to_excel("salidaPCT.xlsx", index=0)

        # print(pctVsPoblacion)
        sns.histplot(data=pctVsPoblacion, x="public_transportation_pct", weights="public_transportation_population",bins=100, kde=False)

        plt.xlabel('Porcentaje')
        plt.ylabel('')
        plt.title('Histograma de Porcentajes VS Población')
        plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter())

        plt.show()



# df = pd.read_csv('public_transportation_statistics_by_zip_code.csv')
# df.dropna(inplace=True)
# df = df[df['public_transportation_pct'] > 0]
# print("DataFrame original:")

