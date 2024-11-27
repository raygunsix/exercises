import glob
from pathlib import Path
from fpdf import FPDF


filepaths = glob.glob("data-animals/*.txt")
pdf = FPDF(orientation="portrait", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem
    title = filename.capitalize()

    with open(filepath, 'r') as file:
        content = file.read()
    
    pdf.add_page()

    # Add title
    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=50, h=8, txt=title, ln=1)

    # Add body
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output/output.pdf")