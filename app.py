from pdf2image import convert_from_path
import os
import shutil


def pdfTopng():
     os.mkdir('converted_files')
     try:
          images = convert_from_path('arquivo.pdf', poppler_path=r'..\Simply_PDF_to_JPG\poppler-0.68.0\bin')
          for i in range(len(images)):
               print(i)
               images[i].save(f'converted_files/image_{i+1}.png','PNG')
     except:
          ...

if __name__ == '__main__':
     try:
          shutil.rmtree('converted_files')
     except:
          ...
     pdfTopng()