

with open('answers') as file:

    sumOfAnswers = 0
    answersOfGroup = []
    for collectedAnswers in file:
        if collectedAnswers == '\n':
            uniqueAnswers = set(answersOfGroup)
            sumOfAnswers += len(uniqueAnswers)
            answersOfGroup = []
            print(f"Unique answers: {uniqueAnswers}")
        answersOfGroup = answersOfGroup + [answer for answer in collectedAnswers if answer != '\n']

    print(f"Sum of answers: {sumOfAnswers}")