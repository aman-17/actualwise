import fitz
import io
import os
from PIL import Image
import pytesseract


from pypdf import PdfReader

reader = PdfReader("2306.03341.pdf")

def read_images():
    reader = PdfReader("2306.03341.pdf")
    page = reader.pages[0]
    count = 0

    for image_file_object in page.images:
        with open(str(count) + image_file_object.name, "wb") as fp:
            fp.write(image_file_object.data)
            count += 1
    print(count)


def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    image_list = []
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base = os.path.splitext(pdf_path)[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:   
                pix._writeIMG("p%s.png" % (i,))
            else:             
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1._writeIMG("p%s.png" % (i,))
                pix1 = None
            pix = None
            image_list.append("p%s.png" % (i,))
    return image_list

def ocr_core(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text

def extract_text_from_images_in_pdf(pdf_file):
    images = extract_images_from_pdf(pdf_file)

    text = ''
    for image in image:
        text += ocr_core(image)
        os.remove(image)
    return text

pdf_file = '2306.03341.pdf'

text = extract_text_from_images_in_pdf(pdf_file)
print(text)

