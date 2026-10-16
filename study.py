server_logs = [
    "INFO: User 123 logged in",
    "ERROR: Database connection timeout",
    "WARNING: CPU load at 85%",
    "ERROR: Invalid token received",
    "INFO: Payment processed"
]

def extract_errors(logs):
    for log in logs:
        if "ERROR" in log:
            yield log
            
generator_object = extract_errors(server_logs)
for error in generator_object:
    print(error)
    
    
transactions = [
    {"id": 1, "amount": 150.0, "status": "success"},
    {"id": 2, "amount": 20.0, "status": "failed"},
    {"id": 3, "amount": 99.99, "status": "success"},
    {"id": 4, "amount": 500.0, "status": "failed"}
]

def get_failed_transactions(tx_lists):
    for transaction in tx_lists:
        if transaction.get("status") == "failed":
            yield transaction

generator_transaction = get_failed_transactions(transactions)
for status in generator_transaction:
    print(status)