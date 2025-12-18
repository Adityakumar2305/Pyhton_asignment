
import csv
from pathlib import Path

TXT_FILE = "sales.txt"
CSV_FILE = "sales.csv"

# 1) Create sales.txt and store daily sales records

initial_records = [
    "2025-12-18 | Phone Case | 3 | 299.0",
    "2025-12-18 | Charger     | 2 | 799.0",
    "2025-12-18 | Earbuds     | 1 | 2499.0",
]

with open(TXT_FILE, "w", encoding="utf-8") as f:
    for line in initial_records:
        f.write(line.strip() + "\n")

print("Created sales.txt and wrote initial sales records.\n")


# 2) Append new sales data to sales.txt

new_record = "2025-12-18 | Screen Guard | 5 | 149.0"
with open(TXT_FILE, "a", encoding="utf-8") as f:
    f.write(new_record + "\n")

print(" Appended new sales record to sales.txt:", new_record, "\n")


print(" Contents of sales.txt after append:")
with open(TXT_FILE, "r", encoding="utf-8") as f:
    print(f.read())


# 3) Convert sales.txt to sales.csv

# Target CSV headers
fieldnames = ["Date", "Item", "Quantity", "Price", "Amount"]

def parse_txt_line(line):

    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 4:
        return None  # malformed line
    date, item, qty_str, price_str = parts[:4]
    try:
        qty = float(qty_str)
        price = float(price_str)
        amount = qty * price
        return {"Date": date, "Item": item, "Quantity": qty, "Price": price, "Amount": amount}
    except ValueError:
        return None

rows = []
with open(TXT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parsed = parse_txt_line(line)
        if parsed:
            rows.append(parsed)

# Write to CSV
with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for r in rows:
        writer.writerow({
            "Date": r["Date"],
            "Item": r["Item"],
            "Quantity": int(r["Quantity"]) if r["Quantity"].is_integer() else r["Quantity"],
            "Price": r["Price"],
            "Amount": r["Amount"],
        })

print("\n Converted sales.txt → sales.csv\n")


# 4) Read and display all records from sales.csv

print(" Records in sales.csv:")
with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# 5) Calculate total sales amount from sales.csv
total_amount = 0.0
with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:

        try:
            if "Amount" in row and str(row["Amount"]).strip() != "":
                total_amount += float(row["Amount"])
            else:
                q = float(row.get("Quantity", 0))
                p = float(row.get("Price", 0))
                total_amount += q * p
        except ValueError:

            pass


