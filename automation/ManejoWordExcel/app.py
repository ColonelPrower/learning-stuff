from docx import Document

document = Document()

document.add_paragraph("Este es un parrafo automatizado")

document.save("ejemplo.docx")
