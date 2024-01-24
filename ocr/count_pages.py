from pdf2image import convert_from_path

images = convert_from_path('./Case_study_1_CO.pdf')
for i, image in enumerate(images):
    image.save(f'./casestudy1/image_{i+1}.png', 'PNG')