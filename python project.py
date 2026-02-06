balance = 0  # initial balance
recharge_history = []  # to store mobile numbers and amounts

# keep looping until user exits
while True:
    print("\n--- Mobile Recharge System ---")
    print("1. Check Balance")
    print("2. Recharge")
    print("3. View Recharge History")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your Current Balance = Rs.", balance)

    elif choice == 2:
        # use a for loop to allow multiple recharges in one go
        times = int(input("How many recharges do you want to do? "))
        for i in range(times):
            mobile = input(f"Enter mobile number for recharge {i+1}: ")
            amount = int(input(f"Enter recharge amount {i+1}: "))
            balance += amount
            recharge_history.append((mobile, amount))
            print(f"Recharge {i+1} successful! Rs.{amount} added for {mobile}.")
        print("Total Balance after recharges = Rs.", balance)

    elif choice == 3:
        if recharge_history:
            print("\n--- Recharge History ---")
            for idx, (mobile, amount) in enumerate(recharge_history, start=1):
                print(f"{idx}. Mobile: {mobile}, Amount: Rs.{amount}")
        else:
            print("No recharges done yet.")

    elif choice == 4:
        print("Thank you for using Mobile Recharge System")
        break

    else:
        print("Invalid choice, please try again.")

