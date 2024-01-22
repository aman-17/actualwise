from deidentify.base import Document
from deidentify.taggers import FlairTagger
from deidentify.tokenizer import TokenizerFactory

# Create some text
# text = (
#     "Dit is stukje tekst met daarin de naam Jan Jansen. De patient J. Jansen (e: "
#     "j.jnsen@email.com, t: 06-12345678) is 64 jaar oud en woonachtig in Utrecht. Hij werd op 10 "
#     "oktober door arts Peter de Visser ontslagen van de kliniek van het UMCU."
# )


text = ("D Blood Glucose Monitoring Stack 11:42 10/28 Stop: 12:07 10/28 Admin Sched"
"NOW 10/28 12:07 11:42 Not Administered/Nc agarin"
"Other - See Notes"
"iva"
"D Care Profile and Crisis Plan Siac: 11:42 10/28 Stop: 12:04 10/28 Admin Sched"
"EVERY 4 HOURS - UNTIL COMPLETE. 10/28 12:04 11:42 Complete agarin"
"D CBC W/O DIFFERENTIAL ‘Mac: 10:00 10/29 Stop: 0:47 10/30 Admin Sched"
"EVERY MORNING UNTIL COMPLETE 10/29 16:01 10:00 Not Adminietered/Nckslupek"
"D COMPREHENSIVE METABOLIC ‘Start: 10:00 10/29 Stop: 0:47 10/30 Admin Sched"
"EVERY MORNING UNTIL COMPLETE, 10/29 16:01 10:00 Not Administered/Nc kslupek"
"Qiher - See Notes,"
"DD Consent and Declination of Seasonal Influenza ‘Siac 11:42 10/28 Stop: 12:01 10/28 Admin ‘Sched"
"‘Vaceine 10/28 12:01 11:42 Complete agarin"
"EVERY 12 HOURS UNTIL COMPLETE"
"A COWS Scale ‘Stat: 17:00 10/28 Stop: 23:59 12/31 Admin Sched"
"Every 4 hours - COWS 10/28 17:03 17:00 Complete kslupek"
"If initial score >10 assess vitals per protocol Verify 10/28 21:10 21:00 Complete mebree"
"with MD the imitiation of the medical detox 10/29 9:56 9:00 Complete keslnpek"
"protocol. 10/29 12:56 13:00 Complete eslopek"
"10/29 16:02 17:00 Complete kslupek"
"10/29 21:14 21:00 Complets sjohn"
"10/30 &15 9:00 Complete rsoriano"
"‘A Daily Nursing Progress Note ‘Stact 16:00 10/28 Stop: 23:59 12/31 ‘Admin ‘Sched"
"Twice a Day Assessments 10/28 12:07 16:00 Not Administered/Nc agarin"
"Other - See Notes"
"see admission assessment"
"10/29 1:32 4:00 Complete amebreo"
"10/29 14:55 16:00 Complete kslupek"
"10/29 23:22 4:00 Complete sjohn"
"10/30 10:30 16:00 Complete jlundang"
"A Environment Patient Safety Checklist Stadt 16:00 10/28 Stop: 23:59 12/31 Admin Sched"
"‘Twioe a Day Assessments 10/28 12:07 16:00 Complete agarin"
"10/28 21:08 4:00 Complete amebreo"
"10/29 14:55 16:00 Complete kalupek"
"10/29 23:18 4:00 Complete sjohn"
"D Initial Nursing Assessment ‘Start 11:42 10/28 Stop: 12:37 10/28 Admin Sched"
"EVERY 4 HOURS - UNTIL COMPLETE. 10/28 12:36 11:42 Complete agarin"
"D Initial Treatment Plan Staci: 11:42 10/28 Stop: 12:10 10/28 Admin Sched"
"EVERY 4 HOURS - UNTIL COMPLETE 10/28 12:10 11:42 Complete agacin"
"D hnitiate Treatment Plan for Patient ‘Siac: 11:42 10/28 Stop: 13:52 10/28 Admin ‘Sched"
"EVERY 4 HOURS - UNTIL COMPLETE 10/28 13:52 11:42 Complete agarin"
"D LIPID PANEL W/HDL ‘Start: 10:00 10/29 Stop: 10:19 10/30 Admin Sched"
"EVERY MORNING UNTIL COMPLETE, 10/29 16:01 10:00 Not Administered/Nc kslupek"
"Other - See Notes"
"10/30 10:19 10:00 _Complete rsoriano"
"D Patient Unit Orientation Checklist Stadt 11:42 10/28 Stop: 12:02 10/28 Admin Sched"
"EVERY 4 HOURS - UNTIL COMPLETE. 10/28 12:02 11:42 Complete agarin"
"D Safety and Health Evaluation Start: 11:42 10/28 Stop: 12:09 10/28 Admin Sched"
"Onc time for ancillary orders 10/28 12:09 11:42 _ Complete agarin"
"A. buprenorphine TABLET 2mg Stadt 10:00 10/30 Stop: 23:59 12/31 Admin Sched"
"(*Subutex) 10/30 10:12 10:00 Complete rsoriano"
"Sublingnal TWICE DAILY 0900 & 1700"
"for Maintenance"
""
"printed: 10/30/23 12:37 Page 1 of 3")

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