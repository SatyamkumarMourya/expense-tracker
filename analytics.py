import numpy as np

def calculate_statistics(expenses):
    if not expenses:
        return 0,0,0,0
    amounts = np.array([expense["amount"] for expense in expenses])

    total = np.sum(amounts)
    average = np.mean(amounts)
    highest = np.max(amounts)
    lowest = np.min(amounts)

    return total, average, highest, lowest
