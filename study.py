incoming_request = {
    "username": "maksim",
    "age": "twenty-five" 
}

try:
    age = int(incoming_request["age"])
    print(f"Age update to {age}")
except KeyError:
    print("Error: Missing 'age' field")
except ValueError as error_message:
    print(f"Error: Invalid data type. Details: {error_message}")