import csv
import os

INPUT_FILE = "/app/data/transactions-to-send.csv"
OUTPUT_FILE = os.environ.get(
    "OUTPUT_FILE",
    "/app/data/processed/transactions-processed.csv"
)
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(INPUT_FILE, newline="", encoding="utf-8") as source:
    reader = csv.DictReader(source)
    rows = list(reader)
    fieldnames = reader.fieldnames

if not fieldnames:
    raise ValueError("Invalid or empty CSV file")

processed = 0
rejected = 0

for row in rows:
    try:
        amount = float(row["amount"])
        if amount > 0:
            row["status"] = "PROCESSED"
            processed += 1
        else:
            row["status"] = "REJECTED"
            rejected += 1
    except (ValueError, KeyError):
        row["status"] = "REJECTED"
        rejected += 1

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as output:
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Processed transactions: {processed}")
print(f"Rejected transactions: {rejected}")
print(f"Output saved: {OUTPUT_FILE}")