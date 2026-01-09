from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Union
from bson import ObjectId

class MongoDBConnectionError(Exception):
    uri = "mongodb+srv://python_testing_user:PythonUser89@cluster0.oiurzgx.mongodb.net/?appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    db = client["quickcut_db"]
    collection = db["Similar_article_to_test"]

    def __init__(self):
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client["quickcut_db"]
        self.collection = self.db["Similar_article_to_test"]
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def fetch_articles_by_created_date(self,days: int = 0) -> List[Dict]:
        """
        Fetch articles created in the last `days` days using createdAt field
        """
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
        end_date = cutoff_date + timedelta(days=0)
        query = {
            "createdAt": {
                "$lte": cutoff_date
            }
        }

        projection = {
            "_id": 1,
            "title": 1,
            "summary": 1,
            "content": 1
        }

        return list(self.collection.find(query, projection))


    def delete_article_by_id(self, article_id: Union[str, ObjectId]) -> bool:
        """
        Delete article by _id.
        Returns True if deleted, False otherwise.
        """
        result = self.collection.delete_one({"_id": article_id})
        return result.deleted_count == 1

    def closeconn(self):
        """
        Close the MongoDB connection
        """
        self.client.close()
        print("MongoDB connection closed.")
