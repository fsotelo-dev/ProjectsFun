# ============================================
#   💰 BUDGET TRACKER — Intro Python Project
# ============================================
# Concepts you'll practice:
#   - Lists & dictionaries
#   - Functions
#   - Loops & conditionals
#   - String formatting
#   - User input
# ============================================

transactions = []  # This is our "database" — a list of dictionaries


# ---------- CORE FUNCTIONS ----------

def add_transaction(category, amount, transaction_type):
    """Add an income or expense to the tracker."""
    transaction = {
        "category": category,
        "amount": amount,
        "type": transaction_type  # "income" or "expense"
    }
    transactions.append(transaction)
    print(f"\n  ✅ Added: {transaction_type.capitalize()} — {category} ${amount:.2f}\n")


def get_balance():
    """Calculate total income, total expenses, and net balance."""
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expenses
    return total_income, total_expenses, balance


def show_summary():
    """Print a formatted summary of all transactions."""
    if not transactions:
        print("\n  No transactions yet!\n")
        return

    print("\n" + "=" * 40)
    print("  📊 BUDGET SUMMARY")
    print("=" * 40)

    print("\n  💚 INCOME:")
    for t in transactions:
        if t["type"] == "income":
            print(f"    + ${t['amount']:>8.2f}  —  {t['category']}")

    print("\n  🔴 EXPENSES:")
    for t in transactions:
        if t["type"] == "expense":
            print(f"    - ${t['amount']:>8.2f}  —  {t['category']}")

    total_income, total_expenses, balance = get_balance()
    print("\n" + "-" * 40)
    print(f"  Total Income:   ${total_income:>8.2f}")
    print(f"  Total Expenses: ${total_expenses:>8.2f}")
    print("-" * 40)

    if balance >= 0:
        print(f"  ✅ Net Balance:  ${balance:>8.2f}  — you're in the green!")
    else:
        print(f"  ⚠️  Net Balance: -${abs(balance):>7.2f}  — watch your spending!")

    print("=" * 40 + "\n")


def show_menu():
    """Print the main menu."""
    print("\n" + "─" * 40)
    print("  💰 BUDGET TRACKER")
    print("─" * 40)
    print("  1. Add Income")
    print("  2. Add Expense")
    print("  3. View Summary")
    print("  4. Quit")
    print("─" * 40)


def get_amount(prompt):
    """Ask user for an amount and validate it's a positive number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("  ❌ Amount must be greater than 0. Try again.")
            else:
                return amount
        except ValueError:
            print("  ❌ Please enter a valid number (e.g. 50 or 12.99).")


# ---------- MAIN PROGRAM LOOP ----------

def main():
    print("\n  Welcome to your Budget Tracker! 🎉")
    print("  Track your income and expenses easily.\n")

    # Load some sample data so it's not empty on start
    add_transaction("Paycheck", 1500.00, "income")
    add_transaction("Freelance", 200.00, "income")
    add_transaction("Rent", 700.00, "expense")
    add_transaction("Groceries", 85.50, "expense")
    add_transaction("Netflix", 15.99, "expense")

    while True:
        show_menu()
        choice = input("  Choose an option (1–4): ").strip()

        if choice == "1":
            print("\n  -- ADD INCOME --")
            category = input("  Category (e.g. Paycheck, Freelance, Gift): ").strip()
            amount = get_amount("  Amount: $")
            add_transaction(category, amount, "income")

        elif choice == "2":
            print("\n  -- ADD EXPENSE --")
            category = input("  Category (e.g. Rent, Food, Gas): ").strip()
            amount = get_amount("  Amount: $")
            add_transaction(category, amount, "expense")

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("\n  See you later! Keep budgeting. 💪\n")
            break

        else:
            print("\n  ❌ Invalid option. Please enter 1, 2, 3, or 4.")


# ---------- RUN IT ----------
if __name__ == "__main__":
    main()


# ============================================
#  🚀 CHALLENGE IDEAS — try these next!
# ============================================
# 1. Add a "delete transaction" option
# 2. Let the user filter by category (e.g. show only food expenses)
# 3. Save transactions to a .txt or .csv file so they persist
# 4. Add a monthly budget limit and warn when close to it
# 5. Show a spending breakdown by category (% of total expenses)
# ============================================