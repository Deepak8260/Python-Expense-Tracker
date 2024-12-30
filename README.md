Expense Tracker Application
===========================

Overview
--------

The **Expense Tracker Application** is a simple Python-based tool to help you track your expenses over time. You can log new expenses, view your expenses, and get a report of the total amount spent. The application stores all the data in a JSON file, making it easy to persist and manage your expense records.

Features
--------

*   **Log Expense**: Allows you to add a new expense with details such as category, amount, and date.
    
*   **View Expenses**: Displays all logged expenses along with the total amount spent.
    
*   **Persistent Data**: The application stores your expenses in a JSON file, ensuring your data is saved between sessions.
    

Prerequisites
-------------

*   Python 3.x or higher
    
*   Basic knowledge of Python programming
    

No additional packages or dependencies are required to run the application.

Getting Started
---------------

### Step 1: Clone the Repository

You can download or clone the repository to your local machine:

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### Step 2: Navigate to the Project Directory

Go to the project directory:

```bash
cd expense-tracker
```

### Step 3: Run the Application

To run the application, use the following command:

```bash
python tracker.py
```


The application will start and present you with a simple menu to interact with.

How to Use the Application
--------------------------

### Menu Options:

Upon starting the program, you will be presented with a menu. You can choose from the following options:

1.  **Log Expense**: Add a new expense by providing the category, amount, and date.
    
2.  **View Expenses**: View a list of all logged expenses, including the total amount spent.
    
3.  **Exit**: Exit the program.
    

### Logging an Expense:

When you choose to log an expense, the program will prompt you to enter:

*   **Category**: The category of the expense (e.g., "Food", "Transport").
    
*   **Amount**: The amount of the expense.
    
*   **Date**: The date of the expense in YYYY-MM-DD format.
    

### Viewing Expenses:

When you choose to view your expenses, the program will show you a list of all the logged expenses, including:

*   Date of the expense.
    
*   Category of the expense.
    
*   Amount of the expense.It will also display the **total amount** of all expenses.
    

### Exiting the Application:

You can exit the application by selecting option **3\. Exit**.

Example Usage
-------------

### 1\. Log an Expense

When the application starts, select **1** to log a new expense:

```bash
Expense Tracker Application
1. Log Expense
2. View Expenses
3. Exit

Enter your choice: 1
Enter the expense category: Food
Enter the amount: 50.5
Enter the date (YYYY-MM-DD): 2024-01-15
Expense of 50.5 in category Food added successfully.
```

### 2\. View Logged Expenses

Next, select **2** to view your logged expenses:

```bash
Expense Tracker Application
1. Log Expense
2. View Expenses
3. Exit

Enter your choice: 2
2024-01-15 | Food | 50.5
Total amount: 50.5

```

### 3\. Exit the Application

To exit, simply select **3**:

```bash
Expense Tracker Application
1. Log Expense
2. View Expenses
3. Exit

Enter your choice: 3
Exiting the Expense Tracker. Goodbye!

```


Data Storage
------------

The application stores expenses in a JSON file named expenses.json. This file will be created automatically when the program is run for the first time. All the logged expenses will be saved in this file, and you can view them later.

### Example of expenses.json

Here is an example of how the expenses.json file might look:

```bash
[
    {
        "category": "Food",
        "amount": 50.5,
        "date": "2024-01-15"
    },
    {
        "category": "Transport",
        "amount": 20.0,
        "date": "2024-01-16"
    }
]

```


File Structure
--------------

```bash
expense-tracker/
│
├── tracker.py        # Main Python file for the application logic
├── expenses.json     # JSON file storing the expense data
└── README.md         # This README file

```


Customizing the Application
---------------------------

If you'd like to extend or modify the application, here are a few ideas:

*   Add the ability to edit or delete an expense.
    
*   Include a feature to filter expenses by category or date range.
    
*   Implement data validation for inputs (e.g., ensuring the amount is a positive number).
    

Troubleshooting
---------------

*   **Error**: "No such file or directory: 'expenses.json'"
    
    *   **Solution**: This error occurs if the expenses.json file does not exist. The program will automatically create this file when you log your first expense.
        

Contributing
------------

Feel free to contribute to this project by submitting bug reports, feature requests, or even code improvements! To contribute, fork the repository, create a branch, and submit a pull request with your changes.

License
-------

This project is open-source and available under the MIT License.

Contact
-------

For any questions or feedback, feel free to reach out to me at \[kd.codegeek@gmail.com\].
