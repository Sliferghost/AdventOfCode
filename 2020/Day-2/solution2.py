
def toRange(input):
    split = input.split('-')
    return range(int(split[0]), int(split[1]))

def isValidPassword(policyRange, policyCharacters, password):
    firstCharacterEqual = password[policyRange.start] == policyCharacters
    secondCharacterEqual = password[policyRange.stop] == policyCharacters
    
    if(firstCharacterEqual and not secondCharacterEqual): return True
    elif(secondCharacterEqual and not firstCharacterEqual): return True
    return False


countValidPasswords = 0

with open('password-list') as file:
    for line in file:
        split = line.strip().split(':')
        policy = split[0]
        policyRange = toRange(policy.split(' ')[0])
        policyCharacters = policy.split(' ')[1]
        password = split[1]
        if(isValidPassword(policyRange, policyCharacters, password)):
            countValidPasswords += 1

print(f"Amount of valid passwords: {countValidPasswords}")