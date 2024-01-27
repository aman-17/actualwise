from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("nlpie/clinical-distilbert-i2b2-2010")
model = AutoModelForMaskedLM.from_pretrained("nlpie/clinical-distilbert-i2b2-2010")
nlp=pipeline(task="ner", model="obi/deid_bert_i2b2")

def chunk_text(text, chunk_size=512):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def deidentify_text(text, ner_results):
    sorted_entities = sorted(ner_results, key=lambda x: x['start'])
    merged_entities = []

    for entity in sorted_entities:
        if merged_entities and entity['start'] <= merged_entities[-1]['end']:
            merged_entities[-1]['end'] = max(merged_entities[-1]['end'], entity['end'])
            merged_entities[-1]['entity'] = entity['entity']
        else:
            merged_entities.append(entity)

    deidentified_text = text
    for entity in reversed(merged_entities):
        start = entity['start']
        end = entity['end']
        deidentified_text = deidentified_text[:start] + "[" + entity['entity'] + "]" + deidentified_text[end:]
    return deidentified_text

example = "ABCD is a male."


chunks = chunk_text(example)

deidentified_chunks = []
for chunk in chunks:
    ner_results = nlp(chunk)
    deidentified_chunk = deidentify_text(chunk, ner_results)
    deidentified_chunks.append(deidentified_chunk)

deidentified_text = "".join(deidentified_chunks)
print(deidentified_text)

