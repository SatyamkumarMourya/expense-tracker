# Expense Tracker 💰

A command-line expense management application built with Python. The project allows users to record, view, search, and analyze their expenses while storing data locally in a JSON file.

## 📌 About the Project

The Expense Tracker was built to practice Python programming fundamentals while developing a practical, modular application.

The project separates different responsibilities into multiple Python modules, making the code easier to understand, maintain, and extend.

## ✨ Features

* Add new expenses
* View recorded expenses
* Search and filter expenses
* Calculate total expenses
* Organize expenses by category
* Record expense amount, category, and date
* Validate user input
* Handle invalid input safely
* Save and load expense data using JSON
* Separate application logic into multiple modules

## 🛠️ Technologies Used

* Python 3
* JSON
* Lists and dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* Modular programming

## 📂 Project Structure

```text
Expense Tracker/
│
├── Expense Tracker.py
├── expense_manager.py
├── storage.py
├── validation.py
├── expenses.json
└── README.md
```

### `Expense Tracker.py`

The main entry point of the application. It handles the main program flow and user interaction.

### `expense_manager.py`

Contains the core expense-management functionality, such as adding, viewing, searching, and calculating expenses.

### `storage.py`

Handles saving and loading expense data using JSON.

### `validation.py`

Contains validation functions used to check user input before processing it.

### `expenses.json`

Stores the expense records locally in JSON format.

### `README.md`

Contains documentation and information about the project.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in a terminal.
3. Run the main Python file:

```bash
python "Expense Tracker.py"
```

## 🧾 Example Expense Data

An expense record contains information such as:

```python
{
    "amount": 150,
    "category": "Food",
    "date": "26-09-26"
}
```

## 📊 Example

If the tracker contains:

```text
Food      ₹150
Food      ₹100
Travel    ₹100
```

The total expense is:

```text
₹350
```

## 🎯 What I Learned

This project helped me practice:

* Writing reusable Python functions
* Working with lists and dictionaries
* Processing structured data
* Handling user input
* Using exception handling
* Reading and writing JSON files
* Separating functionality into modules
* Building a complete command-line application

## 🚀 Future Improvements

Possible future improvements include:

* Monthly expense reports
* Category-based spending analysis
* Budget tracking
* Data visualization
* Graphical user interface
* Database integration
* Exporting expense reports to CSV

## 👨‍💻 Author

**Satyamkumar Mourya**

BCA — Artificial Intelligence & Machine Learning
