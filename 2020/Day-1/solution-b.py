expenses = []

with open('expense_report') as file:
    for expense in file:
        expenses.append(int(expense.rstrip()))

for firstLoopExpense in expenses:
    for secondLoopExpense in expenses:
        for thirdLoopExpense in expenses:
            if firstLoopExpense == secondLoopExpense == thirdLoopExpense:
                continue
            if firstLoopExpense + secondLoopExpense + thirdLoopExpense == 2020:
                print(f"Found the expenses: {firstLoopExpense}, {secondLoopExpense}, and {thirdLoopExpense}")
                print(f"Solution = {firstLoopExpense * secondLoopExpense * thirdLoopExpense}")
                exit()
