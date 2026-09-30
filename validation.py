import datetime

def get_valid_amount(prompt):
    while True:
        try:
            amount=float(input(prompt))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount")

def get_non_empty_input(prompt):
    while True:
        data=input(prompt).strip()
        if not data:
            print("This field cannot be empty")
        else:
            return data
        
def get_valid_date():
    while True:
        try:
            year=int(input("Enter year : "))
            month=int(input("Enter month : "))
            day=int(input("Enter day : "))
            date=datetime.date(year, month, day)
            date_string=date.isoformat()
            return date_string
        except ValueError:
            print("Invalid Input, Check your input before entering")