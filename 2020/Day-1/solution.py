expenses = []

with open('expense_report') as file:
    for expense in file:
        expenses.append(int(expense.rstrip()))

for outerLoopExpense in expenses:
    for innerLoopExpense in expenses:
        if outerLoopExpense == innerLoopExpense:
            continue
        if outerLoopExpense + innerLoopExpense == 2020:
            print(f"Found the expenses: {outerLoopExpense} and {innerLoopExpense}")
            print(f"Solution = {outerLoopExpense * innerLoopExpense}")
            exit()