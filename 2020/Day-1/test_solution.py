from solution import findExpenses

def test_findExpenses_single_expense():
    expenseReport = [1]
    expenses = findExpenses(expenseReport, 2)
    assert expenses == 1

def test_findExpenses_multiple_expenses():
    expenseReport = [1,2,3,4,5]
    expenses = findExpenses(expenseReport, 6)
    assert expenses == 5


# expenses = []

# with open('expense_report') as file:
#     for expense in file:
#         expenses.append(int(expense.rstrip()))