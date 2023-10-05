from pdf2docx import Converter
pdf_file = 'Daniel Sana CV Official.pdf'
docx_file = 'Daniel Sana CV Official.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()