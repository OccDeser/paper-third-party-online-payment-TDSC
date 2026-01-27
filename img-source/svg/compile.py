import os
import subprocess
from tqdm import tqdm
from pathlib import Path
from typing import List
import sys

def find_svg_files(path: str | Path = ".") -> List[Path]:
  path = Path(path)
  return sorted(path.glob("*.svg"))

def convert2pdf(svg_path: Path, pdf_path: Path) -> None:
  tqdm.write(f"Converting {svg_path} to {pdf_path}...")
  subprocess.run([
    r"C:\Program Files\Inkscape\bin\inkscape.exe",
    svg_path,
    "--export-type=pdf",
    f"--export-filename={pdf_path}"
  ], check=True)

if not sys.argv[1:]:
  svgs = find_svg_files()
else:
  svgs = [Path(arg) for arg in sys.argv[1:]]

for svg in tqdm(svgs):
  pdf = svg.with_suffix(".pdf")
  pdf = os.path.join("..", "..", "img", pdf.name)
  convert2pdf(svg, pdf)



