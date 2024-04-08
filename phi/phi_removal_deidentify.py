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

# text = ("David Smith, a 39-year-old male, came in for his routine check-up on May 15, 2024. Residing at 2356 Oak Street, Lincoln, NE, 68502, he has been a patient under the care of Dr. John Doe (JDge) for the past five years. During this visit, David mentioned experiencing mild, intermittent chest discomfort over the past month. He has a family history of heart disease, as noted in his previous records. His mother, Julia Smith, had @ myocardial infarction at the age of 65. David's vitals were within normal limits, with a blood pressure reading of 130/85 mmHg. Dr. Doe recommended a stress test and an EKG to evaluate David's cardiac function, considering his family history and symptoms. The patient's social security number 987- 65-4321 was used for records. His medical record number RC20240515-247 was updated with these new findings. David's insurance information, Meridian (ID: M-55502-47), was confirmed. jdoe advises a heart- healthy diet and consider starting 4 low-impact exercise regimen. A follow-up appointment was scheduled for six months later to reassess his condition.")

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
pprint(first_doc.annotations)
from deidentify.util import mask_annotations

masked_doc = mask_annotations(first_doc)
print(masked_doc.text)
print(tagger.tags)