import pandas as pd
from docx import Document

# leer excel

df = pd.read_excel("excel.xlsx")

# crear un nuevo documento word
document = Document()

# Agregar una tabla al docuento con el numero de columnas basado en el Dataframe
table = document.add_table(rows=1, cols=len(df.columns))
hdr_cells = table.rows[0].cells

# Asignar los nombres de las columnas al encabezado de la tabla
for i, column in enumerate(df.columns):
    hdr_cells[i].text = column

# Agregar cada fila del Dataframe a la tabla
for index, row in df.iterrows():
    row_cells = table.add_row().cells
    for i, item in enumerate(row):
        row_cells[i].text = str(item)

document.save("reporte.docx")
