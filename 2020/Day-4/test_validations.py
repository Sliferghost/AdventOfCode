from solution2 import *

def test_validateBirthYear_lowerBound():
    assert validateBirthYear("1920") == True
def test_validateBirthYear_upperBound():
    assert validateBirthYear("2002") == True
def test_validateBirthYear_tooLow():
    assert validateBirthYear("1919") == False
def test_validateBirthYear_tooHigh():
    assert validateBirthYear("2003") == False
def test_validateBirthYear_invalidCharacters():
    assert validateBirthYear("ABCD") == False


def test_validateIssueYear_lowerBound():
    assert validateIssueYear("2010") == True
def test_validateIssueYear_upperBound():
    assert validateIssueYear("2020") == True
def test_validateIssueYear_tooLow():
    assert validateIssueYear("2009") == False
def test_validateIssueYear_tooHigh():
    assert validateIssueYear("2021") == False
def test_validateIssueYear_invalidCharacters():
    assert validateIssueYear("ABCD") == False


def test_validateExpirationYear_lowerBound():
    assert validateExpirationYear("2020") == True
def test_validateExpirationYear_upperBound():
    assert validateExpirationYear("2030") == True
def test_validateExpirationYear_tooLow():
    assert validateExpirationYear("2019") == False
def test_validateExpirationYear_tooHigh():
    assert validateExpirationYear("2031") == False
def test_validateExpirationYear_invalidCharacters():
    assert validateExpirationYear("ABCD") == False


def test_validateHeight_cm_lowerBound():
    assert validateHeight("150cm") == True
def test_validateHeight_cm_upperBound():
    assert validateHeight("193cm") == True
def test_validateHeight_cm_tooLow():
    assert validateHeight("149cm") == False
def test_validateHeight_cm_tooHigh():
    assert validateHeight("194cm") == False
def test_validateHeight_in_lowerBound():
    assert validateHeight("59in") == True
def test_validateHeight_in_upperBound():
    assert validateHeight("76in") == True
def test_validateHeight_in_tooLow():
    assert validateHeight("58in") == False
def test_validateHeight_in_tooHigh():
    assert validateHeight("77in") == False
def test_validateHeight_missingIndicator():
    assert validateHeight("151") == False
def test_validateHeight_missingNumber():
    assert validateHeight("cm") == False
    

def test_validateHairColor_validColor():
    assert validateHairColor("#123abc") == True
def test_validateHairColor_missingHashtag():
    assert validateHairColor("123abc") == False
def test_validateHairColor_tooFewCharacters():
    assert validateHairColor("#12345") == False
def test_validateHairColor_tooManyCharacters():
    assert validateHairColor("#1234567") == False
def test_validateHairColor_invalidHexidecimalCharacters():
    assert validateHairColor("#123abz") == False

def test_validateEyeColor_validColors():
    for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        assert validateEyeColor(color) == True
def test_validateEyeColor_invalidColor():
    assert validateEyeColor("Boe") == False


def test_validatePassportID_validID():
    assert validatePassportID("123456789") == True
def test_validatePassportID_tooFewNumbers():
    assert validatePassportID("12345678") == False
def test_validatePassportID_tooManyNumbers():
    assert validatePassportID("1234567890") == False
def test_validatePassportID_invalidCharacters():
    assert validatePassportID("a23456789") == False