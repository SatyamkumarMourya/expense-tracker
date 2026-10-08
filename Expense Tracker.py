from storage import load_expenses
from expense_manager import calculate_total, display_expenses, add_expense, update_expense, delete_expense, search_by_category, search_by_description, search_by_date, category_summary, monthly_summary, view_expenses
from analytics import calculate_statistics
from pandas_analytics import pandas_monthly_summary, pandas_category_summary, calculate_monthly_statistics, calculate_category_statistics, calculate_monthly_changes, show_calculated_monthly_changes
from visualization import show_category_chart, show_monthly_chart

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
        print("13.Category Chart")
        print("14.Monthly Chart")
        print("15.Monthly Analytics")
        print("16.Category Statistics")
        print("17.Exit")
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
            trans_count, total, average, median, highest, lowest = calculate_statistics(expenses)
            print("===== EXPENSE ANALYTICS =====")
            print("Total no. of Transactions :", trans_count)
            print("Total expense :", total)
            print("Average expense :", average)
            print("Median expense :", median)
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
            show_category_chart(expenses)
        elif opt==14:
            show_monthly_chart(expenses)
        elif opt==15:
            monthly = pandas_monthly_summary(expenses)
            monthly = calculate_monthly_changes(monthly)
            
            count, total, average, median, highest, lowest, highest_month, lowest_month = calculate_monthly_statistics(monthly)
            print("===== MONTHLY EXPENSE ANALYTICS =====")
            print("Total no. of Months:", count)
            print("Total monthly expense :", total)
            print("Average monthly expense :", average)
            print("Median monthly expense :", median)
            print("Highest monthly expense :", highest)
            print("Highest spending month :", highest_month)
            print("Lowest monthly expense :", lowest)
            print("Lowest spending month :", lowest_month)
            print()
            show_calculated_monthly_changes(monthly)
        elif opt==16:
            hcategory, hcatspent, lcategory, lcatspent, fcategory, fcount, hpercentcat, hpercent = calculate_category_statistics(expenses)
            print("===== CATEGORY STATISTICS =====")
            print("Highest spending category : ",hcategory)
            print("Highest Spending : ",hcatspent)
            print("Least spending category : ",lcategory)
            print("Least Spending : ",lcatspent)
            print("Most Frequent Category : ",fcategory)
            print("Frequency of frequent category : ",fcount)
            print("Highest percentage category coverage : ",hpercentcat)
            print("Highest category percent : ",hpercent,"%")
        elif opt==17:
            print("Thanks for using our Program")
            break
        else:
            print("Invalid option selected, Choose from options available")
            
if __name__ == "__main__":
    main()
            
