from pdf2image import convert_from_path

images = convert_from_path('./CaseStudy_2_SD.pdf')
for i, image in enumerate(images):
    image.save(f'./casestudy2/image_{i+1}.png', 'PNG')
