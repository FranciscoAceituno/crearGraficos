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
        print("Resumen Potenciales clientes")
        print("**"*35)

        totalPoblacionUsoTransporte = round(sales_data['public_transportation_population'].sum(),2)
        print(f'\nTotal población usa transporte público --> {totalPoblacionUsoTransporte}' )

        totalPoblacion = round(sales_data['totalPoblacion'].sum(),0)
        print(f'Total de la población --> {totalPoblacion}' )

        posiblesClientes = sales_data[sales_data['public_transportation_pct'] > 40]

        
        pctPosiblesClientes = round((posiblesClientes['public_transportation_population'].sum() / posiblesClientes['totalPoblacion'].sum())*100,2 )
        print(f'\nPorcentaje de potenciales clientes {pctPosiblesClientes}% *')

        cantPosiblesClientes = posiblesClientes['public_transportation_population'].sum()
        print(f'Cantidad de potenciales clientes {cantPosiblesClientes} *')
        print('\n\n*Este porcentaje y número se obtuvo considerando que dentro del\ncódigo postal el uso del transporte sea superior al 40%')
        

        input('\nPresione una tecla para ver el gráfico...')

        # Paso 4: Crear un diagrama de dispersión
        # Graficar el primer diagrama de dispersión en el primer subplot (ax1)
        fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(12, 6))  # 1 fila, 2 columnas
        ax1.scatter(sales_data['totalPoblacion'],sales_data['public_transportation_pct'], alpha=0.5, color='blue')
        ax1.set_title('Uso de Transporte Público vs Porcentaje de uso sin filtrar')
        ax1.set_xlabel('Cantidad de Habitantes')
        ax1.set_ylabel('Porcentaje de Uso de Transporte Público')
        ax1.xaxis.set_major_locator(plt.MultipleLocator(5000))
        ax1.yaxis.set_major_locator(plt.MultipleLocator(5)) 
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))

        # Graficar el segundo diagrama de dispersión en el segundo subplot (ax2)
        ax2.scatter(posiblesClientes['totalPoblacion'],posiblesClientes['public_transportation_pct'], alpha=0.5, color='red')
        ax2.set_title(f'Gráfico que presenta los Potenciales clientes\n corresponde al {pctPosiblesClientes} % del total de la población')
        ax2.set_xlabel('Cantidad de Habitantes')
        ax2.set_ylabel('Porcentaje de Uso de Transporte Público')
        ax2.xaxis.set_major_locator(plt.MultipleLocator(5000))
        ax2.set_ylim(0, 110)
        ax2.yaxis.set_major_locator(plt.MultipleLocator(10)) 
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))


        # Ajustar automáticamente el diseño de los subplots
        plt.tight_layout()

        # Mostrar los gráficos
        plt.show()

        # Paso 5: Exportar los datos a un archivo Excel
        posiblesClientes = posiblesClientes.sort_values(by='zip_code', ascending=True)
        output_file_path = "Resultado Analisis posibles ventas.xlsx" 
        posiblesClientes.to_excel(output_file_path, index=False)