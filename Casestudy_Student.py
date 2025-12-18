
FILENAME = "students.txt"

# 1. Create a file and write student records
records = [
    "Aditya Kumar, 101, Electronics",
    "Priya Sharma, 102, Computer Science",
    "Rahul Verma, 103, Mechanical"
]
with open(FILENAME, "w", encoding="utf-8") as f:
    for r in records:
        f.write(r + "\n")
print("File created and records written.\n")

# 2. Read and display all contents
print("Reading file contents:")
with open(FILENAME, "r", encoding="utf-8") as f:
    print(f.read())

# 3. Append a new student record
new_record = "Neha Patil, 104, Civil"
with open(FILENAME, "a", encoding="utf-8") as f:
    f.write(new_record + "\n")
print("\nAppended new record:", new_record)

# Show contents after append
print("\nContents after append:")
with open(FILENAME, "r", encoding="utf-8") as f:
    print(f.read())

# 4. Count total number of lines (records)
with open(FILENAME, "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)
print(f"\nTotal student records: {count}")

# 5. Search for a student name
search_name = "Aditya"
matches = []
with open(FILENAME, "r", encoding="utf-8") as f:
    for line in f:
        if search_name.lower() in line.lower():
            matches.append(line.strip())

print(f"\nSearch results for '{search_name}':")
if matches:
    for m in matches:
               print("-", m)
else:
    print("No matches found.")

