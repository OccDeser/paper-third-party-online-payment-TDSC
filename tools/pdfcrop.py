import os

os.chdir('../img')
for f in os.listdir():
    if os.path.splitext(f)[0] in ['file-name']:
        os.system('pdfcrop ' + f + ' ' + f)