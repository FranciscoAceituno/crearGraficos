import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import hist
import numpy as np
from funcionesCross import Funciones
from histograma import Histograma
from graficoDispersion import GraficoDispersion

class ProcessFile:

    df = any
    def __init__(self, dfInicial) -> None:
        self.funciones= Funciones()
        self.df = dfInicial
        self.histogram = Histograma(self.df)
        self.dispersion = GraficoDispersion(self.df)

    def menuPrincipal(self) -> None:
        try:
            while True:
                os.system('cls||clear')
                print("***  Electromobility Plus  ***")
                print("*"*40)
                print("\n¿Qué desea hacer?")
                print("1. Obtener Porcentajes Mínimo y Máximo")
                print("2. Ventas potenciales promedio Alto Transporte y Bajo Transporte")
                print("3. Crear Histograma")
                print("4. Crear gráfico de disperción")
                print("5. Salir")
                
                opcion = int(input("Ingrese su opción: ").strip(' \n\t'))
                
                match int(opcion):
                    case 1:
                        self.get_min_max_pct()
                    case 2:
                        self.getPotentialSeal()
                    case 3:
                        self.histogram.createHistogram()
                    case 4:
                        self.dispersion.crearGrafico()
                    case 5:
                        self.salir()
                    case _:
                        raise Exception("Opción inválida. Intente nuevamente.")
                    
        except Exception as e:
            if 'invalid literal for int()' in str(e):
                self.funciones.make_it_flash('Solo se permiten numeros....')
            else:
                self.funciones.make_it_flash(str(e))
            self.menuPrincipal()


    def get_min_max_pct(self):

        os.system('cls||clear')
        pctMin = self.df['public_transportation_pct'].min()
        pctMax = self.df['public_transportation_pct'].max()

        print('Los porcentajes máximo y mínimo son: ')
        print('*'*40)
        print(f'Mínimo : {pctMin} \r')
        print(f'Máximo : {pctMax} \r')
        print()
        input('presione una tecla para volver al menú anterior....')

    def getPotentialSeal(self):
        os.system('cls||clear')
         #alto transporte publico
        dfPromedioAltoTrans = self.df.query('public_transportation_pct > 10')
        promedioAltoUso = round(dfPromedioAltoTrans['public_transportation_population'].mean(),2)

        dfPromedioBajoTrans = self.df.query('public_transportation_pct <= 10')
        promedioBajoUso = round(dfPromedioBajoTrans['public_transportation_population'].mean(),2)

        print('Las ventas potenciales promedio: ')
        print('*'*40)
        print(f'Mínimo : {promedioBajoUso} \r')
        print(f'Máximo : {promedioAltoUso} \r')
        print()
        input('presione una tecla para volver al menú anterior....')


    def salir(self) -> None:
        self.funciones.make_it_flash("¡Hasta luego!")
        os.system('cls||clear')
        sys.exit()