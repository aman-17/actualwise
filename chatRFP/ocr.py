from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re
import os


oem_val = 3  # Example OEM value
psm_val = 6  # Example PSM value - 3, 4, 6? 1, 5, 7, 11, 12 (6 is best for Case 1)
custom_config = f'--oem {oem_val} --psm {psm_val}'

pdf_path = 'chatRFP/CityofCasselberry_RRCRHDraft.pdf'

output_folder = 'chatRFP/ocr_output/'
pdf_base_name = os.path.splitext(os.path.basename(pdf_path))[0]

output_file_name = f"{pdf_base_name}_oem{oem_val}_psm{psm_val}_pytesseract_poppler_dpi600.txt"
output_file_path = os.path.join(output_folder, output_file_name)

def clean_embedded_page_numbers(text):
    return re.sub(r'Page\s+\d+', '', text)

images = convert_from_path(pdf_path, 600)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, config=custom_config)
        cleaned_text = clean_embedded_page_numbers(text)
        # Inserting PDF page number
        output_file.write(f'PDF Page Number {i + 1}\n{cleaned_text}\n\n' + '-'*60 + '\n')

print(f"OCR text saved to {output_file_path}")