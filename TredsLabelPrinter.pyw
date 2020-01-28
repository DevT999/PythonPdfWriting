import PySimpleGUI as sg
import subprocess

from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF
from datetime import date

def watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
 
    pdf = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
 
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

## write a date on pdf

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


layout = [[sg.Text('Select a style')],
          [sg.Radio('17', "Style", default=True), sg.Radio('12', "Style"), sg.Radio('6', "Style")],
		  [sg.Text('Select a size')],
		  [sg.Radio('XXL', "Size"), sg.Radio('XL', "Size"), sg.Radio('L/XL', "Size"), sg.Radio('L', "Size"), sg.Radio('M/L', "Size"), sg.Radio('M', "Size"), sg.Radio('S', "Size"), sg.Radio('XS', "Size")],
          [sg.Button('Print')] ]

window = sg.Window('TREDS Label Printer', layout)

size = list("10850")

while True:  # Event Loop
    event, values = window.Read()
    ## 17 radio button
    if values[0] == True:
        size[1] = "7"
        styletxt = '17" High'
    ## 12 radio button
    if values[1] == True:
        size[1] = "4"
        styletxt = '12" Mid'
    ## 6 radio button
    if values[2] == True:
        size[1] = "3"
        styletxt = '6" Low' 
    ## XXL radio button
    if values[3] == True:
        size[4] = "4"
        sizetxt = "XXL"
    ## XL radio button
    if values[4] == True:
        size[4] = "3"
        sizetxt = "XL"
    ## LXL radio button
    if values[5] == True:
        size[4] = "5"
        sizetxt = "L/XL"
    ## L radio button
    if values[6] == True:
        size[4] = "2"
        sizetxt = "L"
    ## ML radio button
    if values[7] == True:
        size[4] = "6"
        sizetxt = "M/L"
    ## M radio button
    if values[8] == True:
        size[4] = "1"
        sizetxt = "M"
    ## S radio button
    if values[0] == True:
        size[4] = "0"
        sizetxt = "S"
    ## XS radio button
    if values[9] == True:
        size[4] = "9"
        sizetxt = "XS"
    if event is None or event == 'Exit':
        break
    if event == 'Print':
        print(size)
        sku = "".join(size)
        print(sku)

        ## set file path
        case_filename = 'C:/Users/APC-B1/Documents/Labels/case/' + sku + '.pdf'

        ## output temp file
        if __name__ == '__main__':
            watermark(input_pdf=case_filename, 
                    output_pdf='temp_case.pdf',
                    watermark_pdf='test.pdf')

        printlabel = sg.PopupYesNo(f'Do you want to print a {sku} {styletxt} {sizetxt}')  # Shows Yes and No buttons
        if printlabel == "Yes":
            subprocess.call(['C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\Foxit Reader.exe', '/t', output_pdf, 'Case'])
            subprocess.call(['C:\\Program Files (x86)\\Foxit Software\\Foxit Reader\\Foxit Reader.exe', '/t', f'C:/Users/APC-B1/Documents/Labels/single/{sku}.pdf', 'Labels'])
window.Close()
