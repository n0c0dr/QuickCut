from .engine import get_category_trends
from .similarityCheck import find_and_delete_similar_articles

if __name__ == "__main__":
    # print("\n🏏 SPORTS (India)")
    # print(get_category_trends("sports", region="india"))

    # print("\n💹 STOCKS (India)")
    # print(get_category_trends("stocks", region="india"))

    # print("\n🚀 SCIENCE (World)")
    # print(get_category_trends("science", region="world"))

    # print("\n🏛 POLITICS (kolkata)")
    # print(get_category_trends("politics", region="state", state="kolkata"))

    # print(similarity_check("Apple releases new iPhone", "New iPhone launched by Apple"))
    print("\nDeleted Articles IDs:")
    print(find_and_delete_similar_articles(threshold=0.75))
