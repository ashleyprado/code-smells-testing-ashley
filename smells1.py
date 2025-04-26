"""
Refactored smells1.py
Run tests with: pytest tests/smells1_test.py
"""

# Define prices as constants
ITEM_PRICES = {
    "apple": 1.00,
    "banana": 0.50,
    "cherry": 0.75,
    "mango": 1.00,
    "pineapple": 1.50,
    "dragonfruit": 2.00,
    "durian": 2.75,
}

DISCOUNT_THRESHOLD = 10
DISCOUNT_RATE = 0.9

def calculate_total_price(items):
    total = 0
    for item in items:
        price = ITEM_PRICES.get(item)
        if price is not None:
            total += price
        else:
            print(f"Unknown item: {item}")

    total = apply_discount_if_needed(total)
    return total

def apply_discount_if_needed(total):
    if total >= DISCOUNT_THRESHOLD:
        return total * DISCOUNT_RATE
    return total

if __name__ == "__main__":
    print("Run `pytest tests/smells1_test.py` instead.")
