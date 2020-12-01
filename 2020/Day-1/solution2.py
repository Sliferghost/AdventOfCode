from typing import List

def findExpenses(expensesReport: List[int], expenseTotal: int) -> int:
    for firstLoopExpense in expensesReport:
        for secondLoopExpense in expensesReport:
            for thirdLoopExpense in expensesReport:
                if firstLoopExpense + secondLoopExpense + thirdLoopExpense == expenseTotal:
                    return firstLoopExpense * secondLoopExpense * thirdLoopExpense