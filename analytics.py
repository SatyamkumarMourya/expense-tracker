import numpy as np

def calculate_statistics(expenses):
    if not expenses:
        return 0,0,0,0,0,0
    amounts = np.array([expense["amount"] for expense in expenses])

    transaction_count = len(expenses)
    total = np.sum(amounts)
    average = np.mean(amounts)
    highest = np.max(amounts)
    lowest = np.min(amounts)
    median = np.median(amounts)

    return transaction_count, total, average, median, highest, lowest
