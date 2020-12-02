
def toRange(input):
    split = input.split('-')
    return range(int(split[0]), int(split[1]))

def isValidPassword(policyRange, policyCharacters, password):
    countPolicyCharactersInPassword = password.count(policyCharacters)
    return (countPolicyCharactersInPassword >= policyRange.start and
            countPolicyCharactersInPassword <= policyRange.stop)


countValidPasswords = 0

with open('password-list') as file:
    for line in file:
        split = line.split(':')
        policy = split[0]
        policyRange = toRange(policy.split(' ')[0])
        policyCharacters = policy.split(' ')[1]
        password = split[1]
        if(isValidPassword(policyRange, policyCharacters, password)):
            countValidPasswords += 1

print(f"Amount of valid passwords: {countValidPasswords}")