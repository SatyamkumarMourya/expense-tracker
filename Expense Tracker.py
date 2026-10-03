from storage import load_expenses
from expense_manager import calculate_total, display_expenses, add_expense, update_expense, delete_expense, search_by_category, search_by_description, search_by_date, category_summary, monthly_summary, view_expenses
from analytics import calculate_statistics
from pandas_analytics import pandas_monthly_summary, pandas_category_summary

def main():  
    expenses=load_expenses()

    while True:
        print("========== EXPENSE TRACKER =========")
        print("1.Add Expense")
        print("2.View Expense")
        print("3.Calculate Total")
        print("4.Delete expense")
        print("5.Update expense")
        print("6.Search by Category")
        print("7.Search by Description")
        print("8.Category Summary")
        print("9.Search by date")
        print("10.Monthly Summary")
        print("11.Analytics")
        print("12.Pandas Analytics")
        print("13.Exit")
        opt=None
        try:
            opt=int(input("Enter your option number : "))
        except ValueError:
            print("Invalid input entered, Please choose from above given options")
            continue
        
        if opt==1:
            add_expense(expenses)
        elif opt==2:
            view_expenses(expenses)
        elif opt==3:
            print("Total expense : ",calculate_total(expenses))
        elif opt==4:
            delete_expense(expenses)
        elif opt==5:
            update_expense(expenses)
        elif opt==6:
            search_by_category(expenses)
        elif opt==7:
            search_by_description(expenses)
        elif opt==8:
            category_summary(expenses)
        elif opt==9:
            search_by_date(expenses)
        elif opt==10:
            monthly_summary(expenses)
        elif opt==11:
            total, average, highest, lowest = calculate_statistics(expenses)
            print("===== EXPENSE ANALYTICS =====")
            print("Total expense :", total)
            print("Average expense :", average)
            print("Highest expense :", highest)
            print("Lowest expense :", lowest)
        elif opt == 12:
            print("========== PANDAS ANALYTICS ==========")

            monthly = pandas_monthly_summary(expenses)
            category = pandas_category_summary(expenses)

            print("\nMonthly Summary:")
            print(monthly.to_string(index=False))

            print("\nCategory Summary:")
            print(category.to_string(index=False))
        elif opt==13:
            print("Thanks for using our Program")
            break
        else:
            print("Invalid option selected, Choose from options available")
            
if __name__ == "__main__":
    main()
            
