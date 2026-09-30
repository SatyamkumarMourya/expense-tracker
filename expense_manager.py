from storage import save_expenses
from validation import get_valid_amount, get_non_empty_input, get_valid_date

def calculate_total(expenses):
    total=0
    for expense in expenses:
        total=total+expense["amount"]
    return total

def add_expense(expenses):
    expense={}
    amt=get_valid_amount("Enter amount : ")
    cgt=get_non_empty_input("Enter Category : ")
    descp=get_non_empty_input("Enter Description : ")
    date=get_valid_date()
    expense["amount"]=amt
    expense["category"]=cgt
    expense["description"]=descp
    expense["date"]=date
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully")
    
def display_expenses(expenses):
    for index,expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['amount']} | {expense['category']} | {expense['description']} | {expense['date']}")
        
def view_expenses(expenses):
    if not expenses:
        print("No expense record to display")
        return
    display_expenses(expenses)
        
        
def delete_expense(expenses):
    if not expenses:
        print("No expense record to delete")
        return
    display_expenses(expenses)
    try:
        choice=int(input("Enter expense number you want to delete : "))
        index=choice-1
        if 0<= index < len(expenses):
            expenses.pop(index)
            save_expenses(expenses)
            print("Expense deleted successfully")
        else :
            print("Invalid expense number")
    except ValueError:
        print("Invalid choice")
        return
    
def update_expense(expenses):
    if not expenses:
        print("No expense record to update")
        return
    display_expenses(expenses)
    try:
        choice=int(input("Enter expense number you want to update : "))
        index=choice-1
        if 0<= index < len(expenses):
            expense=expenses[index]
            namt=get_valid_amount("Enter new amount : ")
            ncgt=get_non_empty_input("Enter new category : ")
            ndescp=get_non_empty_input("Enter new description : ")
            ndate=get_valid_date()
            expense.update({"amount":namt, "category":ncgt, "description":ndescp, "date":ndate})
            save_expenses(expenses)
            print("Expense updated successfully")
        else:
            print("Invalid expense number")
    except ValueError:
        print("Invalid choice")
        return

def search_by_category(expenses):
    if not expenses:
        print("No expense record to search")
        return
    cgt=input("Enter a category : ").strip().lower()
    if not cgt:
        print("This field cannot be empty")
        return
    found=False
    for expense in expenses:
        if expense["category"].strip().lower() == cgt:
            print(f"{expense['amount']} | {expense['category']} | {expense['description']} | {expense['date']}")
            found=True
    if not found:
        print("No records found of entered category")
        
def search_by_description(expenses):
    if not expenses:
        print("No expense record to search")
        return
    descp_word=input("Enter a keyword to search in description : ").strip().lower()
    if not descp_word :
        print("This field cannot be empty")
        return
    found=False
    for expense in expenses:
        if descp_word in expense["description"].lower():
            print(f"{expense['amount']} | {expense['category']} | {expense['description']} | {expense['date']}")
            found=True
    if not found:
        print("No records found of entered description")
    
def search_by_date(expenses):
    if not expenses:
        print("No expense record present to search")
        return
    sdate=get_valid_date()
    found=False
    for expense in expenses:
        if expense["date"]==sdate:
            print(f"{expense['amount']} | {expense['category']} | {expense['description']} | {expense['date']}")
            found=True
    if not found:
        print("No records found on this date")

def category_summary(expenses):
    if not expenses:
        print("No expense record to summarise")
        return
    category_totals={}
    for expense in expenses:
        cgt=expense["category"].strip().lower()
        if cgt in category_totals:
            category_totals[cgt]+=expense["amount"]
        else :
            category_totals[cgt]=expense["amount"]
            
    for category in category_totals:
        print(category ,":", category_totals[category])
        
def monthly_summary(expenses):
    date=get_valid_date()
    month_expense=[]
    found=False
    for expense in expenses:
        if expense["date"][:7]==date[:7]:
            month_expense.append(expense)
            found=True
    if not found:
        print("No records found for this month")
        return
    category_summary(month_expense)
    print("Total : ",calculate_total(month_expense))


