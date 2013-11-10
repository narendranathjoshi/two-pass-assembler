from symbol_table import *
import re

def addLeadingZeroes(string, length):
    while len(string) <= length:
        string = "0" + string
    return string

def assemble(text):
    #print("Call") #testing #success
    error = {'flag':False, 'type':'', 'lineNo':1}
    errorList = []
    assembled = []
    errorFlag = False
    lineNumber = 1
    for line in text:
        line = re.sub('\s+|,', '*', line)
        line = re.sub('\*+', '*', line)
        line = line.split('*') 
        
        asdLine = ['', ''] #assembled lines       
        #Symbol Table Look-up.
        
        #Opcode
        if line[0] not in symtab_opcode:
            errorFlag = True
            error.update(flag = True, type = 'Invalid OpCode', lineNo = lineNumber)
            errorList.append(error)
        else:
            asdLine[0] += addLeadingZeroes(bin(symtab_opcode.get(line[0]))[2:], 4)
            #print(asdLine) #testing opcode #success
            
        if line[0] is 'swi':
            if line[1] not in symtab_swi:
                errorFlag = True
                error.update(flag = True, type = 'Invalid SWI Code', lineNo = lineNumber)
                errorList.append(error)
            else:
                asdLine[0] += addLeadingZeroes(bin(symtab_swi.get(line[1]))[2:], 2)
                asdLine[0] += '0000000000' #10 unused bits in the end
        
        if line[0] is 'mov':
            if line[1] not in symtab_reg:
                errorFlag = True
                error.update(flag = True, type = 'Invalid Register Specified', lineNo = lineNumber)
                errorList.append(error)
            else:
                asdLine[0] += addLeadingZeroes(bin(symtab_reg.get(line[1]))[2:], 3)
                if '#' in line[2]:
                    asdLine[0] += '1'
                    while len(asdLine[0]) <= 16:
                        asdLine[0] += '0'
                    asdLine[1] = bin(int(line[2][1:]))
                    asdLine[1] = addLeadingZeroes(asdLine[1], 16)
                else:
                    asdLine[0] += addLeadingZeroes(bin(symtab_reg.get(line[2]))[2:], 3)
                    while len(asdLine[0]) <= 16:
                        asdLine[0] += '0'
        assembled.append(asdLine)
    return assembled, errorList, errorFlag
                
        
        
        #print(line) #testing #success