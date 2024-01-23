from deidentify.base import Document
from deidentify.taggers import FlairTagger
from deidentify.tokenizer import TokenizerFactory

# Create some text
# text = (
#     "Dit is stukje tekst met daarin de naam Jan Jansen. De patient J. Jansen (e: "
#     "j.jnsen@email.com, t: 06-12345678) is 64 jaar oud en woonachtig in Utrecht. Hij werd op 10 "
#     "oktober door arts Peter de Visser ontslagen van de kliniek van het UMCU."
# )


text = ("Alice Green, a 48-year-old female, was seen for a surgery consultation on March 10, 2024, with Dr. Emily"
"White (EWhite). Alice, living at 987 Elm Rd, Denver, CO, 80203, has a history of chronic back pain, which"
"has progressively worsened over the past year. During the consultation, Dr. White reviewed Alice's"
"previous treatments, including physical therapy and pain medication, which provided only temporary"
"relief. Alice expressed her concern about the impact of her condition on her daily activities, especially"
"her job as a schoolteacher Her brother, Robert Green, accompanied her and provided additional"
"insights into her reduced mobility and increased dependency on pain medications. An MRI scan taken"
"two weeks prior was reviewed, showing significant disc herniation at L4-L5. Surgery was discussed as @"
"viable option, given the patient's history and current symptoms. Alice's medical record number"
"$C20240310-356 was referenced throughout the consultation. Her insurance details, Medicaid (ID: MD-"
"55503-56), were updated in her file, along with her social security number 234-56-7890. Dr. White"
"advised Alice to consider the surgery, explaining the risks and benefits in detail. A follow-up appointment"
"was scheduled for two weeks later to finalize the decision. Notes were compiled by ewhite.")

# Wrap text in document
documents = [
    Document(name='doc_01', text=text)
]

# Select downloaded model
model = 'model_bilstmcrf_ons_fast-v0.2.0'

# Instantiate tokenizer
tokenizer = TokenizerFactory().tokenizer(corpus='ons', disable=("tagger", "ner"))

# Load tagger with a downloaded model file and tokenizer
tagger = FlairTagger(model=model, tokenizer=tokenizer, verbose=False)

# Annotate your documents
annotated_docs = tagger.annotate(documents)
from pprint import pprint

first_doc = annotated_docs[0]
# pprint(first_doc.annotations)
from deidentify.util import mask_annotations

masked_doc = mask_annotations(first_doc)
print(masked_doc.text)
print(tagger.tags)