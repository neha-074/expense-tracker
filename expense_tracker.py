import csv
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Category", "Amount"])

def add_entry(entry_type):
    category = input("Enter category (food, travel, etc): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([entry_type, category, amount])

    print("✅ Entry added successfully!\n")

def view_summary():
    income = 0
    expense = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Type"] == "Income":
                income += float(row["Amount"])
            else:
                expense += float(row["Amount"])

    print("\n📊 Summary:")
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Balance: {income - expense}\n")

def main():
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_entry("Income")
        elif choice == "2":
            add_entry("Expense")
        elif choice == "3":
            view_summary()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice\n")

main()