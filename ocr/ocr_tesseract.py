# import os
# import pytesseract
# from PIL import Image

# def ocr_core(image):
#     text = pytesseract.image_to_string(Image.open(image))
#     return text

# def extract_text_from_folder(folder_path):
#     files = [f for f in os.listdir(folder_path) if f.endswith(".png") or f.endswith(".jpg")]
#     for i in range(0, len(files), 10):
#         output_file = os.path.join(folder_path, f'output{i//10 + 1}.txt')
#         with open(output_file, 'w') as f:
#             for filename in files[i:i+10]:
#                 image_path = os.path.join(folder_path, filename)
#                 text = ocr_core(image_path)
#                 f.write(f"{text}\n{'-'*30}\n")

# folder_path = './casestudy1'
# extract_text_from_folder(folder_path)

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re
import os

# Directly specify the path to the Poppler bin directory in your script
# poppler_path = r'C:/Program Files/poppler-23.11.0/Library/bin'  # Update this path to your Poppler installation

# Define OEM and PSM values
oem_val = 3  # Example OEM value
psm_val = 6  # Example PSM value - 3, 4, 6? 1, 5, 7, 11, 12 (6 is best for Case 1)
custom_config = f'--oem {oem_val} --psm {psm_val}'

pdf_path = './Case_study_1_CO.pdf'
output_folder = os.path.dirname(pdf_path)
pdf_base_name = os.path.splitext(os.path.basename(pdf_path))[0]
# Construct the output file name to include OEM and PSM values
output_file_name = f"{pdf_base_name}_oem{oem_val}_psm{psm_val}_pytesseract_poppler_dpi600.txt"
output_file_path = os.path.join(output_folder, output_file_name)

# Specify the path to your Tesseract executable if needed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clean_embedded_page_numbers(text):
    # Customize the regex to match your document's embedded page number format
    return re.sub(r'Page\s+\d+', '', text)

images = convert_from_path(pdf_path,600)#,poppler_path=poppler_path)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, config=custom_config)
        cleaned_text = clean_embedded_page_numbers(text)
        # Inserting PDF page number
        output_file.write(f'PDF Page {i + 1}\n{cleaned_text}\n\n')

print(f"OCR text saved to {output_file_path}")