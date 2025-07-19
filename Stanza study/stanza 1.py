import stanza
# stanza.download('it')
nlp = stanza.Pipeline(lang="it")
ner = {}
ent_text = []
with open("hyperskill-dataset-88639758.txt", "r") as reader:
    text = reader.read()
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ':', ent.type)
        ent_text.append(ent.text)
        ner[ent.type] = ent_text
print(ner)
