from PyPDF2 import PdfReader
from pptx import Presentation

def read_files(files):
    raw_text = ""
    for file in files:
        if(file.type == "application/pdf"):
            pdfReader = PdfReader(file)
            for page in pdfReader.pages:
                raw_text += page.extract_text()
        elif(file.type == "application/vnd.openxmlformats-officedocument.presentationml.presentation"):
            prs = Presentation(file)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        raw_text += shape.text  
    return raw_text

# def read_pdf(pdf_files):
#     raw_text = ""
#     for pdf in pdf_files:
#         pdfReader = PdfReader(pdf)
#         for page in pdfReader.pages:
#             raw_text += page.extract_text()
#     return raw_text

# def read_pptx(files):
#     raw_text = ""
#     for pptx in files:
#         prs = Presentation(pptx)
#         for slide in prs.slides:
#             for shape in slide.shapes:
#                 if hasattr(shape, "text"):
#                     raw_text += shape.text
#     return raw_text
