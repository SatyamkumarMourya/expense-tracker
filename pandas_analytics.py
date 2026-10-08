import pandas as pd


def create_dataframe(expenses):
    df = pd.DataFrame(expenses)

    if df.empty:
        return df

    df["date"] = pd.to_datetime(df["date"])

    return df

def pandas_monthly_summary(expenses):
    df = create_dataframe(expenses)

    if df.empty:
        return df

    df["month_year"] = df["date"].dt.to_period("M")

    summary = (df.groupby("month_year")["amount"].sum().reset_index())

    return summary

def pandas_category_summary(expenses):
    df = create_dataframe(expenses)

    if df.empty:
        return df

    summary = (df.groupby("category")["amount"].sum().reset_index())

    return summary


def calculate_monthly_statistics(monthly):
    if monthly.empty:
        return 0, 0, 0, 0, 0, 0, None, None

    amounts = monthly["amount"]

    monthly_count = len(amounts)
    total = amounts.sum()
    average = amounts.mean()
    median = amounts.median()
    highest = amounts.max()
    lowest = amounts.min()

    highest_index = amounts.idxmax()
    lowest_index = amounts.idxmin()

    highest_month = monthly.loc[highest_index, "month_year"]
    lowest_month = monthly.loc[lowest_index, "month_year"]

    return (
        monthly_count,
        total,
        average,
        median,
        highest,
        lowest,
        highest_month,
        lowest_month
    )


def calculate_category_statistics(expenses):
    df = create_dataframe(expenses)

    if df.empty:
        return

    category_spending = df.groupby("category")["amount"].sum()
    category_frequency = df.groupby("category")["amount"].count()
    total_spending = category_spending.sum()
    category_percentage = (category_spending / total_spending) * 100

    highest_category = category_spending.idxmax()
    lowest_category = category_spending.idxmin()
    most_frequent_category = category_frequency.idxmax()
    highest_percentage_category= category_spending.idxmax()
    

    highest = category_spending.max()
    lowest = category_spending.min()
    most_frequent_count = category_frequency.max()
    highest_percentage = category_percentage[highest_percentage_category]

    return highest_category, highest, lowest_category, lowest, most_frequent_category, most_frequent_count, highest_percentage_category, highest_percentage


def calculate_monthly_changes(monthly):
    if monthly.empty:
        return
    
    monthly["previous_amount"] = monthly["amount"].shift(1)
    
    monthly["month_changes"]=monthly["amount"]-monthly["previous_amount"]
    monthly["change_percent"]=(monthly["month_changes"]/monthly["previous_amount"])*100

    return monthly


def show_calculated_monthly_changes(monthly):
    print("Month\t\t Amount\t\t Change\t\t Change %")
    for index in monthly.index:
        if index==0 :
            print(monthly.loc[index, "month_year"],":\t", monthly.loc[index, "amount"],"| First Month, No Previous Data")
        else :
            print(f"{monthly.loc[index, 'month_year']}:\t{monthly.loc[index, 'amount']:.2f}\t|\t{monthly.loc[index, 'month_changes']:.2f}%\t|\t{monthly.loc[index, 'change_percent']:.2f}%")







