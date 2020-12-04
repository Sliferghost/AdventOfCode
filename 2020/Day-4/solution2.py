from validations import validateBirthYear, validateIssueYear, validateExpirationYear, validateHeight, validateHairColor, validateEyeColor, validatePassportID


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
    properties = {property[0]: property[1] for property in (
        passportProperty.split(':') for passportProperty in passport.split(' '))}

    if all(validation(properties.get(property, None)) for (property, validation) in expectedProperties.items()):
        amountOfValidPassports += 1

print(f"Amount of valid passports: {amountOfValidPassports}")
