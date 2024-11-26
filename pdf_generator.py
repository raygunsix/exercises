import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("data-animals/*.txt")

for filepath in filepaths:
    animal = Path(filepath).stem
    print(animal)