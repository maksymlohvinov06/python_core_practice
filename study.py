# incoming_request = {
#     "username": "maksim",
#     "age": "twenty-five" 
# }

# try:
#     age = int(incoming_request["age"])
#     print(f"Age update to {age}")
# except KeyError:
#     print("Error: Missing 'age' field")
# except ValueError as error_message:
#     print(f"Error: Invalid data type. Details: {error_message}")


user_skills = ["Python", "FastAPI", "Docker"]
requested_index = 5

try:
    clean_index = int(requested_index)
    print(f"Requested skill: {user_skills[clean_index]}")
except ValueError:
    print("Enter a valid value")
except IndexError:
    print("Enter a valid index")