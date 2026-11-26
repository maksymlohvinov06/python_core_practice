def calculate_salary(hours, rate):
    salary = hours * rate
    return salary


total = calculate_salary(10, 125)
print(total)

def check_age(age):
    if age >= 18:
        return "Access granted"
    else:
        return "Access denied"


result = check_age(20)
print(result)

numbers = [10, -5, 0, 7, -3, 15, -8, 2]


def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


check = count_positive(numbers)
print(check)

