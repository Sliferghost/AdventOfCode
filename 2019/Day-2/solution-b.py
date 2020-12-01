from typing import List

def intcode_program(memory: List[int]) -> List[int]:
    instructionPointer = 0
    opcode = memory[instructionPointer]

    while opcode != 99:
        opcode = memory[instructionPointer]

        if opcode == 99:
            return memory

        parameter1 = memory[memory[instructionPointer + 1]]
        parameter2 = memory[memory[instructionPointer + 2]]
        position = memory[instructionPointer + 3]

        calculatedValue = 0

        if opcode == 1:
            calculatedValue = parameter1 + parameter2
        elif opcode == 2:
            calculatedValue = parameter1 * parameter2
        else:
            raise ValueError(f"Unsupported opcode {opcode}")

        memory[position] = calculatedValue
        instructionPointer += 4

    return memory

with open("input") as file:
    program = [int(value) for value in file.readline().split(",")]
    
    for noun in range(100):
        for verb in range(100):
            memory = program.copy()
            memory[1] = noun
            memory[2] = verb

            result = intcode_program(memory)
            solution = result[0]
            
            if solution == 19690720:
                print(f"Noun: {noun}, Verb: {verb} == {solution}")
                print(f"Answer = {100 * noun + verb}")
                break