import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import os
import re

# Function to extract names using nltk
def extract_names(text):
    names = []
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                names.append(' '.join(c[0] for c in chunk.leaves()))
    return names

# Function to extract DOB using regex
def extract_dob(text):
    # This pattern will match dates in the format dd/mm/yyyy or dd-mm-yyyy
    pattern = r'\b(0?[1-9]|[12][0-9]|3[01])-/-/\d\d\b'
    dob = re.findall(pattern, text)
    return dob

# Directory containing your text files
directory = './casestudy2/'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as file:
            data = file.read()
            names = extract_names(data)
            dob = extract_dob(data)
            print(f'Names in {filename}: {names}')
            print(f'DOB in {filename}: {dob}')
