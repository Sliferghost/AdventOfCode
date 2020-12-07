

with open('answers') as file:

    sumOfAnswers = 0
    answersOfGroup = []
    peopleInGroup = 0
    for collectedAnswers in file:

        if collectedAnswers == '\n':
            print(f"Amount of people in group: {peopleInGroup}")

            moreThanOnceAnswered = []
            if peopleInGroup == 1:
                moreThanOnceAnswered = answersOfGroup
            else:
                moreThanOnceAnswered = [answer for answer in answersOfGroup if answersOfGroup.count(answer) == peopleInGroup]

            sumOfAnswers += len(set(moreThanOnceAnswered))
            answersOfGroup = []
            peopleInGroup = 0
            print(f"More than once answered: {moreThanOnceAnswered}")
            continue

        answersOfGroup = answersOfGroup + [answer for answer in collectedAnswers if answer != '\n']
        peopleInGroup += 1

    print(f"Sum of answers: {sumOfAnswers}")