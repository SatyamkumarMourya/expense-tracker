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