from sentence_transformers import SentenceTransformer, util
from .utils.mongoconnection import MongoDBConnectionError as con
# Load the model once
model = SentenceTransformer("all-mpnet-base-v2")

def similarity_check(a: str, b: str) -> float:
    emb1 = model.encode(a, convert_to_tensor=True)
    emb2 = model.encode(b, convert_to_tensor=True)
    return util.cos_sim(emb1, emb2).item()


def find_and_delete_similar_articles(threshold=0.70):
    coll = con()
    articles = coll.fetch_articles_by_created_date()   
    print(len(articles))  
    deleted_article = []
    for i in range(len(articles)):
        for j in range(i + 1, len(articles)):
            sim_score = similarity_check(articles[i]['content'], articles[j]['content'])
            
            if sim_score >= threshold:
                print(f"Deleting article content: {articles[j]['content']} (Similarity: {sim_score:.2f})")
                print(f"Deleting article ID: {articles[j]['_id']}")
                deleted_article.append(articles[j]['_id'])
                coll.delete_article_by_id(articles[j]['_id'])
    coll.closeconn()
    return deleted_article
