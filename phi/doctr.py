# from doctr.io import DocumentFile
# from doctr.models import ocr_predictor, from_hub

# img = DocumentFile.from_images(['<image_path>'])
# # Load your model from the hub
# model = from_hub('mindee/my-model')

# # Pass it to the predictor
# # If your model is a recognition model:
# predictor = ocr_predictor(det_arch='db_mobilenet_v3_large',
#                           reco_arch=model,
#                           pretrained=True)

# # If your model is a detection model:
# predictor = ocr_predictor(det_arch=model,
#                           reco_arch='crnn_mobilenet_v3_small',
#                           pretrained=True)

# # Get your predictions
# res = predictor(img)
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

model = ocr_predictor(pretrained=True)
# PDF
doc = DocumentFile.from_pdf("path/to/your/doc.pdf")
# Analyze
result = model(doc)

from doctr.io import DocumentFile