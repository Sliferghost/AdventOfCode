from solution import intcode_program

def test_sum_opcode():
    program = [1,0,0,0,99]
    assert intcode_program(program) == [2,0,0,0,99]

def test_multiply_opcode():
    program = [2,3,0,3,99]
    assert intcode_program(program) == [2,3,0,6,99]

def test_exit_opcode():
    program = [99]
    assert intcode_program(program) == [99]

def test_multiple_lines():
    program = [1,1,1,4,99,5,6,0,99]
    assert intcode_program(program) == [30,1,1,4,2,5,6,0,99]