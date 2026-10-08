import matplotlib.pyplot as plt
from pandas_analytics import create_dataframe
    
def show_category_chart(expenses):
    df = create_dataframe(expenses)
    if df.empty:
        print("No expenses available for chart.")
        return
    summary = df.groupby("category")["amount"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(summary["category"], summary["amount"])
    ax.set_title("Expenses by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Expense (₹)")

    ax.grid()
    plt.show()
    
def show_monthly_chart(expenses):
    df = create_dataframe(expenses)
    if df.empty:
        print("No expenses available for chart.")
        return

    df["date"] = pd.to_datetime(df["date"])
    df["month_year"] = df["date"].dt.to_period("M")

    monthly_summary = df.groupby("month_year")["amount"].sum().reset_index()
    monthly_summary["month_year"] = monthly_summary["month_year"].astype(str)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        monthly_summary["month_year"],
        monthly_summary["amount"],
        marker="o"
    )
    ax.set_title("Monthly Expense Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Expense (₹)")

    ax.grid()
    plt.show()    