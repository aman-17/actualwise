import fitz
from io import BytesIO
from PIL import Image
import pytesseract
import io
import os
# doc = fitz.open("case1.pdf")
# page = doc.load_page(0)

# image_xref = page.get_images()
# xref_value = image_xref[0][0]

# img_dictionary = doc.extract_image(xref_value)
# img_extension = img_dictionary["ext"]
# img_binary = img_dictionary["image"]
# image_io = BytesIO(img_binary)
# image = Image.open(image_io)
# output_path = "image_1.png"
# image.save(output_path)
# image_io.close()

# def ocr_core(image):
#     text = pytesseract.image_to_string(Image.open(image))
#     return text

# def extract_text_from_image(image_file):
#     text = ocr_core(image_file)
#     return text

# text = extract_text_from_image("image_1.png")
# print(text)

import os
import pytesseract
from PIL import Image

def ocr_core(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text

def extract_text_from_folder(folder_path, output_file):
    with open(output_file, 'w') as f:
        for filename in os.listdir(folder_path):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                image_path = os.path.join(folder_path, filename)
                text = ocr_core(image_path)
                f.write(f"{text}\n{'-'*30}\n")

folder_path = './casestudy1'
output_file = './casestudy1/output.txt'
extract_text_from_folder(folder_path, output_file)

