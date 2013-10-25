import symbol_table
from gui import *

'''
data processing insrtuctions
-----------------------------
opcode(4) imm/reg_flag(1) 00 op1(3) op2(3) op3(3) = 16
    op3() reg - 3 bit
    op3() imm - 16 bit in next word
    
data transfer instructions
-----------------------------
opcode(4) op1(3) mem_loc(9) = 16

swi
-----------------------------
opcode(4) int_number(2) 00 0000 0000 = 16

control flow instructions
-----------------------------
opcode(4) label(12) = 16
'''

main() #load and initialize the GUI

#fileName = 'test.asm' #testing