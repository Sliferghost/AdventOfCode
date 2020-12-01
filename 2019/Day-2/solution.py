from typing import List

def intcode_program(program: List[int]) -> List[int]:
    currentIndex = 0
    opcode = program[currentIndex]

    while opcode != 99:
        opcode = program[currentIndex]

        if opcode == 99:
            return program

        firstNumber = program[program[currentIndex + 1]]
        secondNumber = program[program[currentIndex + 2]]
        position = program[currentIndex + 3]

        calculatedValue = 0

        if opcode == 1:
            calculatedValue = firstNumber + secondNumber
        elif opcode == 2:
            calculatedValue = firstNumber * secondNumber
        else:
            raise ValueError(f"Unsupported opcode {opcode}")

        program[position] = calculatedValue
        currentIndex += 4

    return program

with open("input") as file:
    program = [int(value) for value in file.readline().split(",")]
    program[1] = 12
    program[2] = 2
    ranProgram = intcode_program(program)
    print(f"Position 0 {ranProgram[0]}")