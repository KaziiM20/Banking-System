# Banking-System

# 🏦 SKM Bank - Python Banking System

## Overview

SKM Bank is a simple command-line banking system developed in Python. The application allows users to create multiple bank accounts, perform banking transactions, and save account information to a JSON file so that data is retained between program executions.

This project demonstrates the use of object-oriented programming (OOP), file handling, dictionaries, functions, and user interaction in Python.

## Features

- Create multiple bank accounts
- Deposit money
- Withdraw money
- Check account balance
- Prevent duplicate account numbers
- Save account information to a JSON file
- Load existing accounts automatically when the program starts
- Simple menu-driven interface

## Technologies Used

- Python 3
- JSON module

## Project Structure

```
SKM-Bank/
│
├── main.py             # Main banking application
├── accounts.json       # Stores account information
└── README.md           # Project documentation
```
---

## How to Run

1. Install Python 3.
2. Download or clone this project.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python main.py
```

---

## Menu Options

### Main Menu

```
1. Create Account
2. Access Account
3. Exit
```

### Account Menu

```
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
```

## Example

```
=== Welcome to SKM Bank ===

1. Create Account
2. Access Account
3. Exit

Choose an option: 1

Enter your name: John
Enter account number: 1001

Account successfully created!
```

## Concepts Demonstrated

This project demonstrates the following Python concepts:

- Classes and Objects
- Constructors (`__init__`)
- Methods
- Dictionaries
- Functions
- Loops (`while`)
- Conditional Statements (`if`, `elif`, `else`)
- User Input
- File Handling
- JSON Serialization
- Exception Handling

---

## Future Improvements

Possible enhancements include:

- PIN authentication
- Money transfers between accounts
- Transaction history
- Savings and Current account types
- Interest calculation
- Account deletion
- Password encryption
- Graphical User Interface (Tkinter)
- Database integration using SQLite or MySQL
- Online banking with Flask or Django

---

## Author
**Siphokazi Malesa**

## License

This project is for educational purposes and may be modified or expanded for learning and personal use.
