from pdf2image import convert_from_path

images = convert_from_path('./phi3.pdf')
for i, image in enumerate(images):
    image.save(f'./ocr/phiTest/image_{i+1}.png', 'PNG')
