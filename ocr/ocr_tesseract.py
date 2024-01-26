import os
import pytesseract
from PIL import Image

def ocr_core(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text

def extract_text_from_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(".png") or f.endswith(".jpg")]
    for i in range(0, len(files), 10):
        output_file = os.path.join(folder_path, f'output{i//10 + 1}.txt')
        with open(output_file, 'w') as f:
            for filename in files[i:i+10]:
                image_path = os.path.join(folder_path, filename)
                text = ocr_core(image_path)
                f.write(f"{text}\n{'-'*30}\n")

folder_path = './casestudy1'
extract_text_from_folder(folder_path)

