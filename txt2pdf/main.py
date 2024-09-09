import pandas as pd
import glob
from fpdf import FPDF

filepaths=glob.glob(fr'txts\*.txt')
print(filepaths)

pdf = FPDF(orientation='P', unit='mm', format='a4')
pdf.set_auto_page_break(auto=True)

for filepath in filepaths:
    df=open(filepath,'r')
    print(filepath)
    title=filepath.replace('txts',"")
    title=title.strip(r'\\')
    title=title.strip(".txt")
    content=df.readlines()
    print(content)
    x=aaaaaaaa
    pdf.add_page()
    pdf.set_font(family='Arial', style='B', size=16)
    pdf.cell(w=0, h=16, ln=1, border=0, txt=title.capitalize())
    pdf.set_font(family='Times', size=10)
    for line in content:
        pdf.multi_cell(w=0, h=10, txt=line)

pdf.output(fr"pdfs\animal.pdf")
