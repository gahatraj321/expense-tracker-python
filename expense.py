# My first expense calculator

food = 300
transport = 100
coffee = 150

total = food + transport + coffee

print("My total expense today is:", total)
 
print("🎉 Welcome to My Expense Calculator 🎉") 
food = 300
transport = 150
coffee = 100

total = food + transport + coffee

print("-----------------------------")
print("💰 Your total expense today is:", total)
print("-----------------------------")



# Set a daily budget
budget = int(input("Enter your daily budget: "))

# Ask for expenses
food = int(input("Enter food expense: "))
transport = int(input("Enter transport expense: "))
coffee = int(input("Enter coffee expense: "))

# Calculate total
total = food + transport + coffee

# Print total
print("-----------------------------")
print("💰 Your total expense today is:", total)

# Check which category had highest expense
if food >= transport and food >= coffee:
    print("🍔 You spent the most on Food!")
elif transport >= food and transport >= coffee:
    print("🚌 You spent the most on Transport!")
else:
    print("☕ You spent the most on Coffee!")

# Budget warning
if total > budget:
    print("⚠️ Warning! You exceeded your budget by", total - budget, "units.")
else:
    print("✅ Great! You are within your budget.")
print("-----------------------------")



expenses = {}   # store expenses
total = 0

print("🧾 Daily Expense Tracker")
print("Type 'done' to finish entering expenses")
print("----------------------------------")

while True:
    name = input("Enter expense name (food, coffee, etc): ")

    if name.lower() == "done":
        break

    amount = int(input(f"Enter amount for {name}: "))

    expenses[name] = amount
    total += amount

print("----------------------------------")
print("📊 Expense Summary")

for name, amount in expenses.items():
    print(f"{name}: {amount}")

print("----------------------------------")
print("💰 Total expense:", total)

# Highest expense
highest = max(expenses, key=expenses.get)
print("🔥 Highest spending:", highest, "-", expenses[highest])

print("----------------------------------")


expenses ={}
total=0

print(" Daily expense Tracker")
print("type 'done' to finish entering expenses")
print("---------------------------------------")

while True:
    name =input("Enter expense name:")

    if name.lower()=="done":
        break
    amount=int(input(f"Enter amount for {name}:"))
    expenses[name]=amount 
    total+=amount

    print("------------------------------------")
    print("Expense summary")

    for name, amount in expenses.items():
        print(f"{name}: {amount}")
        print("------------------------")
        print("Total expense:",total)

        #Highest expense
        highest =max(expenses, key=expenses.get)
        print("Highest spending:",highest,"-",expenses[highest])

        #save to file
        with open("expenses.txt","a") as file:
            file.write("New Day Expenses\n")
            for name,amount in expenses.item():
                file.write(f"{name}:{amount}\n")
                file.write(f"Total:{total}\n")
                file.write("---------------------\n")

                print("Expenses saved sucessfully")
               
    




