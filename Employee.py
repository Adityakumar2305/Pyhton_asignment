

import csv
from pathlib import Path

FILENAME = "attendance.csv"

# 1) Create a CSV file and write employee attendance data
records = [
    {"EmployeeID": "E001", "Name": "Aditya Kumar", "Date": "2025-12-18", "Status": "Present"},
    {"EmployeeID": "E002", "Name": "Priya Sharma", "Date": "2025-12-18", "Status": "Absent"},
    {"EmployeeID": "E003", "Name": "Rahul Verma", "Date": "2025-12-18", "Status": "Present"},
]

fieldnames = ["EmployeeID", "Name", "Date", "Status"]

# Create/overwrite the file and write header + records
with open(FILENAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(" CSV file created and attendance records written.\n")

# 2) Read and display all records from attendance.csv
print(" Reading all records from attendance.csv:")
with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # Prints as dict: {'EmployeeID': 'E001', 'Name': 'Aditya Kumar', ...}

# 3) Append a new employee attendance record to attendance.csv
new_record = {"EmployeeID": "E004", "Name": "Neha Patil", "Date": "2025-12-18", "Status": "Absent"}

# Ensure header exists (it does, since we created above). Append the new row.
with open(FILENAME, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_record)

print("\n Appended new attendance record:", new_record)

# Show contents after append
print("\n Records after append:")
with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# 4) Count the number of employees marked as "Absent"
absent_count = 0
with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get("Status", "").strip().lower() == "absent":
            absent_count += 1

print(f"\n Total employees marked as Absent: {absent_count}")

## 5) Search for an employee using Employee ID
search_id = "E002"  # you can change this to test
matches = []
with open(FILENAME, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get("EmployeeID", "").strip().lower() == search_id.lower():
            matches.append(row)

print(f"\n Search results for Employee ID '{search_id}':")
if matches:
    for m in matches:
        print(m)
else:
    print("No matches found.")
