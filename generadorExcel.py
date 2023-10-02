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
      self.hoja_excel['A4'] = f"Ejecucion Nro"
      self.hoja_excel['A4'].font = Font(bold=True)
      self.alinearCelda(self.hoja_excel['A4'])
      self.ponerBorde(self.hoja_excel['A4'], self.bordeDelgado)

      self.hoja_excel['B4'].font = Font(bold=True)
      self.hoja_excel['B4'] = f"Tasa de Crecimiento"
      self.alinearCelda(self.hoja_excel['B4'])
      self.ponerBorde(self.hoja_excel['B4'], self.bordeDelgado)

      self.hoja_excel['C4'] = f"Fitness"
      self.hoja_excel['C4'].font = Font(bold=True)
      self.alinearCelda(self.hoja_excel['C4'])
      self.ponerBorde(self.hoja_excel['C4'], self.bordeDelgado)

      # Tamaño columnas
      self.hoja_excel.column_dimensions["A"].width = 20
      self.hoja_excel.column_dimensions["B"].width = 25
      self.hoja_excel.column_dimensions["C"].width = 25

    def alinearCelda(self, celda):
        celda.alignment = Alignment(horizontal='center')

    def ponerBorde(self, celda, borde):
        celda.border = Border(top=borde, left=borde, right=borde, bottom=borde)

    def generar(self, datos, ciclos, caracteres, individuos):
        # Informacion general
        self.hoja_excel['A1'] = f"Cantidad de ciclos: {ciclos}"
        self.hoja_excel['A2'] = f"Cantidad de cromosomas: {caracteres}"
        self.hoja_excel['A3'] = f"Cantidad de individuos por generacion: {individuos}"

        # Se añade estilo a las celdas
        self.hoja_excel['A1'].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel['A1'])
        self.ponerBorde(self.hoja_excel['A1'], self.bordeDelgado)

        self.hoja_excel['A2'].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel['A2'])
        self.ponerBorde(self.hoja_excel['A2'], self.bordeDelgado)

        self.hoja_excel['A3'].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel['A3'])
        self.ponerBorde(self.hoja_excel['A3'], self.bordeDelgado)

        # Se hace merge a las celdas
        self.hoja_excel.merge_cells('A1:C1')
        self.hoja_excel.merge_cells('A2:C2')
        self.hoja_excel.merge_cells('A3:C3')

        # Se llena el excel con los datos
        for ejecucion in range(len(datos)):
            self.hoja_excel[f"A{ejecucion+5}"] = f"Ejecucion {ejecucion+1}"
            self.hoja_excel[f"B{ejecucion+5}"] = datos[ejecucion].flotante
            self.hoja_excel[f"C{ejecucion+5}"] = datos[ejecucion].valorFitness

            # Se le da estilo a las celdas
            self.alinearCelda(self.hoja_excel[f"A{ejecucion+5}"])
            self.alinearCelda(self.hoja_excel[f"B{ejecucion+5}"])
            self.alinearCelda(self.hoja_excel[f"C{ejecucion+5}"])

            self.ponerBorde(self.hoja_excel[f"A{ejecucion+5}"], self.bordeDelgado)
            self.ponerBorde(self.hoja_excel[f"B{ejecucion+5}"], self.bordeDelgado)
            self.ponerBorde(self.hoja_excel[f"C{ejecucion+5}"], self.bordeDelgado)
        
        # Se ponen unas notas al final
        self.hoja_excel[f"A{len(datos)+5}"] = "Mientras mas cerca este el fitness del 1, mas cerca esta de la solucion"
        self.hoja_excel[f"A{len(datos)+6}"] = "Hay muchas soluciones posibles"

        # Se les da estilo
        self.hoja_excel[f"A{len(datos)+5}"].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel[f"A{len(datos)+5}"])
        self.ponerBorde(self.hoja_excel[f"A{len(datos)+5}"], self.bordeDelgado)

        self.hoja_excel[f"A{len(datos)+6}"].font = Font(bold=True)
        self.alinearCelda(self.hoja_excel[f"A{len(datos)+6}"])
        self.ponerBorde(self.hoja_excel[f"A{len(datos)+6}"], self.bordeDelgado)

        # Se hace merge a las celdas
        self.hoja_excel.merge_cells(f"A{len(datos)+5}:C{len(datos)+5}")
        self.hoja_excel.merge_cells(f"A{len(datos)+6}:C{len(datos)+6}")

        # Se guarda el archivo
        self.libro_excel.save(f"{self.directorio_resultados}/resultados {datetime.now().strftime('%d-%m-%Y %H-%M')}.xlsx")

        print(f"Se guardo el archivo en {self.directorio_resultados}/resultados {datetime.now().strftime('%d-%m-%Y %H-%M')}.xlsx")