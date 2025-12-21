from .engine import get_category_trends

if __name__ == "__main__":
    print("\n🏏 SPORTS (India)")
    print(get_category_trends("sports", region="india"))

    print("\n💹 STOCKS (India)")
    print(get_category_trends("stocks", region="india"))

    print("\n🚀 SCIENCE (World)")
    print(get_category_trends("science", region="world"))

    print("\n🏛 POLITICS (Karnataka)")
    print(get_category_trends("politics", region="state", state="Karnataka"))
