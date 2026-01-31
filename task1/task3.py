products = [
    {"name": "Ноутбук", "price": 50000, "category": "Электроника"},
    {"name": "Книга", "price": 500, "category": "Книги"},
    {"name": "Кофе", "price": 300, "category": "Продукты"},
    {"name": "Телефон", "price": 30000, "category": "Электроника"},
    {"name": "Ручка", "price": 50, "category": "Канцтовары"}
]

print('--- Program start ---')

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Products that meet the conditions:")
        output = func(*args, **kwargs)
        for item in output:
            for key, value in item.items():
                print(f"{key}: {value}")
        print('\n')
    return wrapper

@decorator
def filter_by_category(products: list, category: str) -> list:
    return list(filter(lambda x: x["category"] == category, products))

@decorator
def get_expensive_products(products: list, min_price: int) -> list:
    return list(filter(lambda x: x["price"] > min_price, products))

def calculate_total_price(products: list) -> int:
    total_price = 0
    for product in products:
        total_price += product["price"]
    return total_price

"""Testing"""

filter_by_category(products, "Электроника")
filter_by_category(products, "Продукты")

get_expensive_products(products, 450)
get_expensive_products(products, 30000)

print(f"Total price of all products = {calculate_total_price(products)}")

print('--- Program end ---')