from solution import findExpenses

def test_findExpenses_single_expense():
    expenseReport = [1]
    expenses = findExpenses(expenseReport, 2)
    assert expenses == 1



# expenses = []

# with open('expense_report') as file:
#     for expense in file:
#         expenses.append(int(expense.rstrip()))