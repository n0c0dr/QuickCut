from .utils.mongoconnection import MongoDBConnectionError as con
import spacy
nlp = spacy.load("en_core_web_md")

def normalize(text):
    doc = nlp(text)
    return " ".join(
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    )


def similarity_check(phrase1, phrase2):
    doc1 = nlp(normalize(phrase1))
    doc2 = nlp(normalize(phrase2))
    return doc1.similarity(doc2)


def find_and_delete_similar_articles(threshold=0.70):
    coll = con()
    articles = coll.fetch_articles_by_created_date() 
    print(f"Total articles fetched: {len(articles)}")
    print(articles)       
    deleted_article = []
    for i in range(len(articles)):
        for j in range(i + 1, len(articles)):
            sim_score = similarity_check(articles[i]['content'], articles[j]['content'])
            print(f"Article ID: {articles[j]['_id']} (Similarity: {sim_score:.2f})")
            if sim_score >= threshold:
                print(f"Deleting article ID: {articles[j]['_id']}")
                deleted_article.append(articles[j]['_id'])
                coll.delete_article_by_id(articles[j]['_id'])
    coll.closeconn()
    return deleted_article