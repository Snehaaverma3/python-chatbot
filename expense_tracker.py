# Expense tracker project 

expenseslist = [] #list of all expenses iin form of dictionary 
print("welcome to expense tracker")

while True:
   print("===Menu===")
   print("1. Add expense")
   print("2. View all expenses")
   print("3. View total expenses")
   print("4. exit")

   choice = int(input("Enter your choice:"))

   if(choice == 1):
      date= input("Enter the date of expense:")
      category = input("Enter the category of the expense(food, transport, makeup, clothes):")
      description = input("Enter the description of the expense:")
      amount = float(input("Enter the amount of the expense:"))

      expense= {
         "date": date,
         "category": category,
         "description": description,
         "amount": amount
      }

      expenseslist.append(expense)
      print (" \n Expense added successfully")

   elif(choice == 2):
    if len(expenseslist) == 0:
             print("No expenses found:")
    else:
            print("all expenses")
    count = 1
    for eachexpense in expenseslist:
         print(f"expense number {count} -> {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["description"]}, {eachexpense["amount"]}")
         count = count+1
         
   elif(choice == 3):
    total = 0
    for eachexpense in expenseslist:
            total = total + eachexpense["amount"]
            print("\n total expense = ", total)
            
            
   elif(choice == 4):
    print("thank you for using expense tracker")
    break

else:
             print("invalid choice")
