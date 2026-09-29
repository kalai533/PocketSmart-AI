print("Welcome to PocketSmart-AI 💰")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Unakku enna venum (1/2/3): ")

    if choice == "1":
        amount = input("Evlo selavu pannuna? ")
        reason = input("Enna vishayathukku? ")
        expenses.append(f"{reason} - Rs.{amount}")
        print("Saved!")
    elif choice == "2":
        print("\n--- Unoda Selavugal ---")
        for e in expenses:
            print(e)
    elif choice == "3":
        print("Bye Kalaivani! Smart-a save pannu")
        break
      
      
