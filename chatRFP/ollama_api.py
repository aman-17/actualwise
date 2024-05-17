import ollama

input_file = 'chatRFP/ocr_outputs/RFP_2024_1145ActuarialServicesforOPEB 2.29.24_oem3_psm6_pytesseract_poppler_dpi600.txt'

with open(input_file, 'r') as infile:
    data = infile.read()
# print(data)

stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': f'{data}. Based on the above data, answer these questions. What are insurance limits?  How many actives and retirees in the plan? What was last year\'s budget? '}],
    stream=True,
)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)