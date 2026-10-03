from pandas_analytics import create_dataframe,monthly_summary,category_summary

if __name__ == "__main__":
    expenses = [
        {
            "amount": 35.0,
            "category": "travel",
            "description": "house to college",
            "date": "2026-09-28"
        },
        {
            "amount": 35.0,
            "category": "travel",
            "description": "college to house",
            "date": "2026-09-28"
        },
        {
            "amount": 50.0,
            "category": "food",
            "description": "lunch",
            "date": "2026-09-29"
        },
        {
            "amount": 50.0,
            "category": "food",
            "description": "dinner",
            "date": "2026-09-30"
        },
        {
            "amount": 50.0,
            "category": "food",
            "description": "lunch",
            "date": "2026-10-29"
        },
    ]

    print("Monthly Summary:")
    print(monthly_summary(expenses))

    print()

    print("Category Summary:")
    print(category_summary(expenses))