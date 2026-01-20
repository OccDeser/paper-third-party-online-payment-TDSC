import os
import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python replace.py <pdf_directory>")
    sys.exit(1)

pdf_dir = sys.argv[1]
target_dir = "../img/"
# 获取所有PDF文件
pdfs = []
for file in os.listdir(pdf_dir):
    if file.endswith('.pdf'):
        pdfs.append(file)

# 替换对应的图片文件
for pdf in pdfs:
    base_name = os.path.splitext(pdf)[0]
    src_path = os.path.join(pdf_dir, pdf)
    dest_path = os.path.join(target_dir, base_name + '.pdf')
    
    os.remove(dest_path) if os.path.exists(dest_path) else None
    # 复制文件
    shutil.copy2(src_path, dest_path)
    print(f"Replaced: {dest_path}")