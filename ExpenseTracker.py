import csv
def expense():

    categories = {}
    expenses_by_date = {}

    with open("expenses.csv",'r',newline='') as file:
        data = csv.reader(file)
        
        total_expense = 0

        for row in data:

            
            date, category, amount = row

            amount  = int(amount)

            total_expense += amount 
            
            if category not in categories:
                categories[category]= amount
            else:
                categories[category] = categories[category] + amount

            if date not in expenses_by_date:
                expenses_by_date[date] = amount
            else:
                expenses_by_date[date] =  expenses_by_date[date] + amount
        
        highest_expense_date = max(expenses_by_date, key=expenses_by_date.get)
        highest_expense = expenses_by_date.get(highest_expense_date)

       
            
    with open("monthly_summary.txt",'w') as file:
        file.write("Expense Summary (October 2025)\n")
        file.write(f"Total Monthly Expense: {total_expense}")
        file.write("\nCategory-wise Breakdown:\n")
        for category, amount in categories.items():
            file.write(f"{category}      : {amount}\n")
        file.write(f"\nHighest Spending Day: {highest_expense_date} ({highest_expense})")
        file.write("\n")




expense()
