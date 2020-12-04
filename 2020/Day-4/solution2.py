import re

def readPassports():
    passports = []

    with open('passport-batch') as file:
        
        passport = ''
        
        for line in file:
            if line == '\n':
                passports.append(passport.strip())
                passport = ''
            
            passport += line.strip() + ' '
    
    return passports

def dictionaryByGroup(regex, value):
    match = re.fullmatch(regex, value, flags=re.IGNORECASE)
    return match.groupdict()

def validateBirthYear(value):
    try:
        return int(value) in range(1920, 2003)
    except:
        return False

def validateIssueYear(value):
    try:
        return int(value) in range(2010, 2021)
    except:
        return False

def validateExpirationYear(value):
    try:
        return int(value) in range(2020, 2031)
    except:
        return False

def validateHeight(value):
    try:
        values = dictionaryByGroup(r'(?P<value>[0-9]+)(?P<indicator>cm|in)+', value)
        if values['indicator'] == 'cm':
            return int(values['value']) in range(150, 194)
        elif values['indicator'] == 'in': 
            return int(values['value']) in range(59, 77)
        return False
    except:
        return False

def validateHairColor(value):
    try:
        return re.fullmatch(r'#[0-9a-fA-F]{6}', value) != None
    except:
        return False

validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def validateEyeColor(value):
    return value in validEyeColors

def validatePassportID(value):
    try:
        return re.fullmatch(r'[0-9]{9}', value) != None
    except:
        return False

expectedProperties = {
    'byr': validateBirthYear, 
    'iyr': validateIssueYear, 
    'eyr': validateExpirationYear, 
    'hgt': validateHeight, 
    'hcl': validateHairColor, 
    'ecl': validateEyeColor, 
    'pid': validatePassportID
}
passports = readPassports()
amountOfValidPassports = 0

for passport in passports:
    properties = { property[0]: property[1] for property in (passportProperty.split(':') for passportProperty in passport.split(' ')) }

    if all(validation(properties.get(property, None)) for (property, validation) in expectedProperties.items()):
        amountOfValidPassports += 1

print(f"Amount of valid passports: {amountOfValidPassports}")