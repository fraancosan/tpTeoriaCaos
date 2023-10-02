from openpyxl import Workbook
from openpyxl.styles import Border, Side, Font, Alignment
import os
from datetime import datetime


class generadorExcel:
    def __init__(self) -> None:
      # Especifica el directorio donde se guardara el archivo Excel con las posibles soluciones
      self.directorio_resultados = "resultados"

      # Verifica si el directorio existe, de no existir se creara
      if not os.path.exists(self.directorio_resultados):
          os.makedirs(self.directorio_resultados)


      # Crear un nuevo libro de Excel
      self.libro_excel = Workbook()
      self.hoja_excel = self.libro_excel.active
      self.hoja_excel.title = f"Resultados {datetime.now().strftime('%d-%m-%Y %H-%M')}"

      self.bordeDelgado = Side(border_style="thin", color="000000")

      # Instrucciones generales para todos los pasos
      # Encabezados
      self.hoja_excel['A1'] = f"Ejecucion Nro"
      self.hoja_excel['A1'].font = Font(bold=True)
      self.alinearCelda(self.hoja_excel['A1'])
      self.ponerBorde(self.hoja_excel['A1'], self.bordeDelgado)

      self.hoja_excel['B1'].font = Font(bold=True)
      self.hoja_excel['B1'] = f"Tasa de Crecimiento"
      self.alinearCelda(self.hoja_excel['B1'])
      self.ponerBorde(self.hoja_excel['B1'], self.bordeDelgado)

      self.hoja_excel['C1'] = f"Fitness"
      self.hoja_excel['C1'].font = Font(bold=True)
      self.alinearCelda(self.hoja_excel['C1'])
      self.ponerBorde(self.hoja_excel['C1'], self.bordeDelgado)

      # Tamaño columnas
      self.hoja_excel.column_dimensions["A"].width = 20
      self.hoja_excel.column_dimensions["B"].width = 25
      self.hoja_excel.column_dimensions["C"].width = 25

    def alinearCelda(self, celda):
        celda.alignment = Alignment(horizontal='center')

    def ponerBorde(self, celda, borde):
        celda.border = Border(top=borde, left=borde, right=borde, bottom=borde)

    def generar(self, datos):
        # Se llena el excel con los datos
        for ejecucion in range(len(datos)):
            self.hoja_excel[f"A{ejecucion+2}"] = f"Ejecucion {ejecucion+1}"
            self.hoja_excel[f"B{ejecucion+2}"] = datos[ejecucion].flotante
            self.hoja_excel[f"C{ejecucion+2}"] = datos[ejecucion].valorFitness

            # Se le da estilo a las celdas
            self.alinearCelda(self.hoja_excel[f"A{ejecucion+2}"])
            self.alinearCelda(self.hoja_excel[f"B{ejecucion+2}"])
            self.alinearCelda(self.hoja_excel[f"C{ejecucion+2}"])

            self.ponerBorde(self.hoja_excel[f"A{ejecucion+2}"], self.bordeDelgado)
            self.ponerBorde(self.hoja_excel[f"B{ejecucion+2}"], self.bordeDelgado)
            self.ponerBorde(self.hoja_excel[f"C{ejecucion+2}"], self.bordeDelgado)
        
        # Se ponen unas notas al final
        self.hoja_excel[f"A{len(datos)+2}"] = "Mientras mas cerca este el fitness del 1, mas cerca esta de la solucion"
        self.hoja_excel[f"A{len(datos)+3}"] = "Hay muchas soluciones posibles"

        # Se les da estilo
        self.hoja_excel[f"A{len(datos)+2}"].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel[f"A{len(datos)+2}"])
        self.ponerBorde(self.hoja_excel[f"A{len(datos)+2}"], self.bordeDelgado)

        self.hoja_excel[f"A{len(datos)+3}"].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel[f"A{len(datos)+3}"])
        self.ponerBorde(self.hoja_excel[f"A{len(datos)+3}"], self.bordeDelgado)

        # Se hace merge a las celdas
        self.hoja_excel.merge_cells(f"A{len(datos)+2}:C{len(datos)+2}")
        self.hoja_excel.merge_cells(f"A{len(datos)+3}:C{len(datos)+3}")

        # Se guarda el archivo
        self.libro_excel.save(f"{self.directorio_resultados}/resultados {datetime.now().strftime('%d-%m-%Y %H-%M')}.xlsx")

        print(f"Se guardo el archivo en {self.directorio_resultados}/resultados {datetime.now().strftime('%d-%m-%Y %H-%M')}.xlsx")