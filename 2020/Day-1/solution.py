from typing import List

def findExpenses(expensesReport: List[int], expenseTotal: int) -> int:
    for firstLoopExpense in expensesReport:
        for secondLoopExpense in expensesReport:
            if firstLoopExpense + secondLoopExpense == expenseTotal:
                return firstLoopExpense * secondLoopExpense