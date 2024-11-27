import glob
from pathlib import Path
from fpdf import FPDF


filepaths = glob.glob("data-animals/*.txt")
pdf = FPDF(orientation="portrait", unit="mm", format="A4")

for filepath in filepaths:
    animal = Path(filepath).stem
    
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=50, h=8, txt=animal.title(), ln=1)

pdf.output("output/output.pdf")