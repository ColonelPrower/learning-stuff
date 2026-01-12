from word_automation import WordAutomation

# Crear una instancia de la biblioteca
doc = WordAutomation("reporte automatizado.docx")

# Agregar un párrafo con formato
doc.agregar_parrafo(
    "Este es un reporte automatizado generado con python.", fuente="Hack", tamano=14
)

# Agregar una tabla desde un archivo Excel
doc.agregar_tabla_desde_excel("excel.xlsx")

# Guardar documento
doc.guardar_documento()
