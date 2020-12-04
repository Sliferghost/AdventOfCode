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

expectedProperties = [
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'#, 'cid'
]
passports = readPassports()
amountOfValidPassports = 0

for passport in passports:
    propertyKeys = [ property[0] for property in (passportProperty.split(':') for passportProperty in passport.split(' ')) ]
    if all(expectedProperty in propertyKeys for expectedProperty in expectedProperties):
        amountOfValidPassports += 1

print(f"Amount of valid passports: {amountOfValidPassports}")