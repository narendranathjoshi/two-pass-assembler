'''
The List of Operations In Order
=======================
add, sub, mul, mov, b, ble, blt, bgt, bge, beq, 
bne, ldr, str, mla, bl, swi 


The List of Registers in Order
=======================
r0, r1, r2, r3, r4, r5, r6, r7

The List of Software Interrupts
=======================
0x00, 0x01, 0x11, 0x02
'''

opcode_list = ('add', 'sub', 'mul', 'mov', \
               'b', 'ble', 'blt', 'bgt', 'bge',\
                'beq', 'bne', 'ldr', \
                'str', 'mla', 'bl', 'swi')

dpi = ('add', 'sub', 'mul', 'mla')
cfi = ('b', 'ble', 'blt', 'bgt', \
       'bge', 'beq', 'bne', 'bl')
dti = ('ldr', 'str')

symtab_opcode = {}
bit = 0b0000
for i in opcode_list:
    symtab_opcode[i] = bit
    bit += 0b0001
    #print(i, symtab_opcode.get(i)) #success 
    
reg_list = ('r0', 'r1', 'r2', 'r3', \
            'r4', 'r5', 'r6', 'r7')
symtab_reg = {}
bit = 0b000
for i in reg_list:
    symtab_reg[i] = bit
    bit += 0b001
    #print(i, symtab_reg.get(i)) #success
    
reg_value = 1   

swi_list = ('0x00', '0x01', '0x11', '0x02')
symtab_swi = {}
bit = 0b00
for i in swi_list:
    symtab_swi[i] = bit
    bit += 0b01
    #print(i, symtab_swi.get(i)) #success
    
symtab_labels = {}