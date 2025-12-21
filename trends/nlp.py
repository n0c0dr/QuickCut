import spacy

nlp = spacy.load("en_core_web_sm")

VALID_ENTITIES = {"PERSON", "ORG", "GPE", "EVENT", "PRODUCT"}

def extract_trends(texts):
    phrases = []

    for text in texts:
        doc = nlp(text)

        # Named entities (strongest signal)
        for ent in doc.ents:
            if ent.label_ in VALID_ENTITIES and len(ent.text) > 3:
                phrases.append(ent.text)

        # Noun phrases (context)
        for chunk in doc.noun_chunks:
            if len(chunk.text.split()) >= 2:
                phrases.append(chunk.text)

    return phrases
