
# ==========================================
# 1. Dictionaries: accessing and updating
# ==========================================

user = {
    "username": "maks",
    "age": 22,
    "city": "Kharkiv",
    "balance": 1500
}

print(user["username"])
print(user["city"])

user["balance"] += 500
user["city"] = "Kyiv"
user["is_active"] = True

if "email" in user:
    print(user["email"])
else:
    print("Email не указан")

print(user)


# ==========================================
# 2. Dictionaries: loops and counters
# ==========================================

users = {
    "Alex": 25,
    "Max": 30,
    "Anna": 22,
    "John": 35,
    "Kate": 19
}

count = 0

for name, age in users.items():
    if age > 24:
        print(name)
        count += 1

print(count)


# ==========================================
# 3. Tuples: indexing, slicing and loops
# ==========================================

numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[0:3])

for number in numbers:
    if number > 25:
        print(number)


# ==========================================
# 4. Sets: unique elements and operations
# ==========================================

services = [
    "oil", "brakes", "oil",
    "tires", "brakes", "filters"
]

unique_services = set(services)
unique_services.add("diagnostics")
print(unique_services)

numbers = {10, 20, 30, 40}

numbers.add(50)
numbers.remove(20)
numbers.discard(100)

if 30 in numbers:
    print("Найдено")

print(numbers)
