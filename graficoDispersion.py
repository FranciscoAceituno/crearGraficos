import os
import pandas as pd
import matplotlib.pyplot as plt


class GraficoDispersion:

    df = any
    def __init__(self, dfInicial) -> None:
        self.df = dfInicial
    
    def crearGrafico(self):
        os.system('cls||clear')
        # Paso 2: Agrupar los datos por código postal y calcular el número promedio de ventas estimado
        sales_data = self.df.groupby('zip_code').agg({
            'public_transportation_pct': 'mean',  # Promedio del porcentaje de uso del transporte público
            'public_transportation_population': 'sum'  # Suma de la población que usa transporte público
        }).reset_index()

        # Paso 3: Obtenemos el total de población por cada código postal
        colPoblacionTotal = []
        for p in range(0,len(sales_data.values)):
            listaDatos = sales_data.values[p].tolist()
            poblacionTotal = (listaDatos[2]*100)/listaDatos[1]
            colPoblacionTotal.append(round(poblacionTotal,0))

        # creamos una nueva columna para almacenar el total de la población de cada código postal
        sales_data.insert(3,'totalPoblacion',colPoblacionTotal,True)

        # Presentamos en pantalla los resultados del análisis
        print('Total población usa transporte público --> ', round(sales_data['public_transportation_population'].sum(),2))
        print('total de la población --> ', round(sales_data['totalPoblacion'].sum(),2))
        pctRealUsoTransporte = round((sales_data['public_transportation_population'].sum() / sales_data['totalPoblacion'].sum())*100,2 )
        print('promedio de uso de transporte público --> ', pctRealUsoTransporte)

        # Paso 4: Crear un diagrama de dispersión
        # Graficar el primer diagrama de dispersión en el primer subplot (ax1)
        fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(12, 6))  # 1 fila, 2 columnas
        ax1.scatter(sales_data['totalPoblacion'],sales_data['public_transportation_pct'], alpha=0.5, color='blue')
        ax1.set_title('Relación entre Uso de Transporte Público y Ventas Estimadas por Código Postal')
        ax1.set_xlabel('Cantidad de Habitantes')
        ax1.set_ylabel('Porcentaje de Uso de Transporte Público')
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))

        # Graficar el segundo diagrama de dispersión en el segundo subplot (ax2)

        ax2.scatter(pctRealUsoTransporte, 0, color='red')
        ax2.annotate(f'{pctRealUsoTransporte}%',(pctRealUsoTransporte,0), textcoords="offset points", xytext=(0,10), ha='center')
        ax2.set_xlim(0, 100)
        ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
        ax2.set_title('Gráfico de Análisis de Posibles Ventas')
        ax2.set_xlabel('Porcentaje posibles ventas')
        ax2.get_yaxis().set_visible(False)
        ax2.set_aspect(2.0) 
        ax2.set_xlim(0, 15)  # Ampliar los límites en el eje x
        ax2.set_ylim(-1, 8) 

        # Ajustar automáticamente el diseño de los subplots
        plt.tight_layout()

        # Mostrar los gráficos
        plt.show()

        # Paso 5: Exportar los datos a un archivo Excel
        output_file_path = "Resultado Analisis posibles ventas.xlsx" 
        sales_data.to_excel(output_file_path, index=False)
