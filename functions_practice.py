# def calculate_salary(hours, rate):
#     salary = hours * rate
#     return salary


# total = calculate_salary(10, 125)
# print(total)

# def check_age(age):
#     if age >= 18:
#         return "Access granted"
#     else:
#         return "Access denied"


# result = check_age(20)
# print(result)

# numbers = [10, -5, 0, 7, -3, 15, -8, 2]


# def count_positive(numbers):
#     count = 0
#     for number in numbers:
#         if number > 0:
#             count += 1
#     return count


# check = count_positive(numbers)
# print(check)

products = [
    {"name": "Laptop", "price": 25000, "available": True},
    {"name": "Mouse", "price": 800, "available": True},
    {"name": "Keyboard", "price": 1500, "available": False},
    {"name": "Monitor", "price": 7000, "available": True},
    {"name": "Headphones", "price": 2000, "available": True}
]


def get_available_products(products, max_price):
    list_products = []

    for product in products:
        if product["available"] == True and product["price"] <= max_price:
            list_products.append(product["name"])

    return list_products


check_function = get_available_products(products, 3000)
print(check_function)