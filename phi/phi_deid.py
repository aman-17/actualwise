from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("obi/deid_roberta_i2b2")
model = AutoModelForMaskedLM.from_pretrained("obi/deid_roberta_i2b2")

nlp=pipeline(task="ner", model="obi/deid_roberta_i2b2")

example = "My name is AMAHAD"

ner_results = nlp(example)
# print(ner_results)
