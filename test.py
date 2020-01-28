from fpdf import FPDF
from datetime import date
today = date.today()
d1 = today.strftime("%d")

pdf = FPDF()
pdf.add_page()
pdf.set_xy(97, 111)
pdf.set_font('arial', 'B', 13.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt=d1, border=0)

pdf.set_xy(198.5, 111)
pdf.set_font('arial', 'B', 13.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt=d1, border=0)

pdf.set_xy(97, 264)
pdf.set_font('arial', 'B', 13.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt=d1, border=0)

pdf.set_xy(198.5, 264)
pdf.set_font('arial', 'B', 13.0)
pdf.cell(ln=0, h=5.0, align='L', w=0, txt=d1, border=0)
pdf.output('test.pdf', 'F')