import csv
import os
from datetime import datetime

FILE_PATH = FILE_PATH = os.environ.get("FILE_PATH", "/app/data/transactions.csv")
LOG_PATH = LOG_PATH = os.environ.get("LOG_PATH", "/app/data/error.log")

if not os.path.exists(FILE_PATH):
    print("ERROR: Transaction file not found")
    raise SystemExit(1)

with open(FILE_PATH, newline="") as file:
    rows = list(csv.DictReader(file))

valid_count = 0
invalid_count = 0

with open(LOG_PATH, "a") as log:
    for row in rows:
        try:
            amount = float(row["amount"])
            if amount > 0:
                result = "VALID"
                valid_count += 1
            else:
                result = "INVALID"
                invalid_count += 1
                log.write(
                    f"{datetime.now()} - Invalid transaction: "
                    f"{row['transaction_id']} - Amount: {amount}\n"
                )
        except (ValueError, KeyError):
            result = "INVALID"
            invalid_count += 1
            log.write(
                f"{datetime.now()} - Invalid transaction: "
                f"{row.get('transaction_id', 'UNKNOWN')}\n"
            )

        print(
            f"{row.get('transaction_id')} | "
            f"{row.get('customer_name')} | "
            f"{row.get('amount')} | {result}"
        )

print(f"\nValid transactions: {valid_count}")
print(f"Invalid transactions: {invalid_count}")
print(f"Error log: {LOG_PATH}")
if invalid_count > 0:
    print("QUALITY GATE FAILED: Invalid transactions detected")
    raise SystemExit(1)

print("QUALITY GATE PASSED: All transactions are valid")