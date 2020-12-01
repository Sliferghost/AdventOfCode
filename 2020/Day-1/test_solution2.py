from solution2 import findExpenses
from typing import List

def test_findExpenses_single_expense():
    expenseReport = [1]
    expenses = findExpenses(expenseReport, 3)
    assert expenses == 1

def test_findExpenses_multiple_expenses():
    expenseReport = [1,2,3,4,5]
    expenses = findExpenses(expenseReport, 6)
    assert expenses == 4

def test_findExpenses_find_solution():
    expenseReport = readExpenseReportFromFile()
    expenses = findExpenses(expenseReport, 2020)
    assert expenses == 51810360


def readExpenseReportFromFile() -> List[int]:
    expenses = []

    with open('expense_report') as file:
        for expense in file:
            expenses.append(int(expense.rstrip()))
    
    return expenses