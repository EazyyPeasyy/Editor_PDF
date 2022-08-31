from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color

transparency = Color(245, 0, 0, alpha=0.3)

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
y = 574
can.setLineWidth(7)
can.setStrokeColor(transparency)
can.line(285,y,312,y)
can.drawString(10, 100, "Marcou")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)

existing_pdf = PdfFileReader(open("Padronizadas\DF - Wilson Sons LTD.pdf", "rb"))
output = PdfFileWriter()

page = existing_pdf.getPage(33)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

outputStream = open("resultado.pdf", "wb")
output.write(outputStream)
outputStream.close()