from symbol_table import *
import re

def addLeadingZeroes(string, length):
    while len(string) < length:
        string = "0" + string
    return string

def assemble(text):
    ##print("Call") #testing #success
    error = {'flag':False, 'type':'', 'lineNo':1}
    errorList = []
    assembled = []
    errorFlag = False
    lineNumber = 1
    text = text.split('\n')
    ##print('text: ', text) #testing #success
    for i in text:
        if i is '':
            text.remove(i)
    ##print('text2: ', text) #testing #success
    if text[len(text) - 1] is '':
        text = text[:-1]
    ##print('text3: ', text) #testing #success
    for line in text:
        line = re.sub('\s+|,', '*', line)   #;#print('a', line)
        line = re.sub('\*+', '*', line)     #;#print('b', line)
        line = line.split('*')              #;#print('c', line) 
        line = line[1:]
        ##print('line:', line) #testing #success
        asdLine = '' #assembled lines
        extraLine = '' #the extra line for immediate mode       
        
        #Symbol Table Look-up.
        #Opcode
        if line[0] not in symtab_opcode:
            errorFlag = True
            error.update(flag = True, type = 'Invalid OpCode', lineNo = lineNumber)
            errorList.append(error)
        else:
            asdLine += addLeadingZeroes(bin(symtab_opcode.get(line[0]))[2:], 4)
            #print('opcode:', asdLine) #testing opcode #success
            
        #print("Comes here 49")
        
        #print('swi line:', line[0])
        if line[0] == 'swi':
            
            if line[1] not in symtab_swi:
                errorFlag = True
                error.update(flag = True, type = 'Invalid SWI Code', lineNo = lineNumber)
                errorList.append(error)
            else:
                #print("Comes here 56")
                asdLine += addLeadingZeroes(bin(symtab_swi.get(line[1]))[2:], 2)
                #print('swi1:', asdLine)
                asdLine += '0000000000' #10 unused bits in the end
                #print('swi2:', asdLine)
        
        #print("Comes here 61")
        if line[0] == 'mov':
            if line[1] not in symtab_reg:
                errorFlag = True
                error.update(flag = True, type = 'Invalid Register Specified', lineNo = lineNumber)
                errorList.append(error)
            else:
                asdLine += addLeadingZeroes(bin(symtab_reg.get(line[1]))[2:], 3)
                if '#' in line[2]:
                    asdLine += '1'
                    while len(asdLine) < 16:
                        asdLine += '0'
                    extraLine = bin(int(line[2][1:]))[2:]
                    extraLine = addLeadingZeroes(extraLine, 16)
                    #print('extraline:', extraLine)
                else:
                    if line[2] not in symtab_reg:
                        errorFlag = True
                        error.update(flag = True, type = 'Invalid Register Specified', lineNo = lineNumber)
                        errorList.append(error)
                    else:
                        asdLine += addLeadingZeroes(bin(symtab_reg.get(line[2]))[2:], 3)
                        while len(asdLine) < 16:
                            asdLine += '0'
                #print('mov: ', asdLine)

        if line[0] in dpi:
            if line[1] not in symtab_reg:
                errorFlag = True
                error.update(flag = True, type = 'Invalid Register Specified', lineNo = lineNumber)
                errorList.append(error)
            else:
                asdLine += addLeadingZeroes(bin(symtab_reg.get(line[1]))[2:], 3)
                if line[2] not in symtab_reg:
                    errorFlag = True
                    error.update(flag = True, type = 'Invalid Register Specified', lineNo = lineNumber)
                    errorList.append(error)
                else:
                    asdLine += addLeadingZeroes(bin(symtab_reg.get(line[2]))[2:], 3)
                    if '#' in line[3]:
                        asdLine += '1'
                        while len(asdLine) < 16:
                            asdLine += '0'
                        extraLine = bin(int(line[3][1:]))[2:]
                        extraLine = addLeadingZeroes(extraLine, 16)
                        #print('extraline:', extraLine)
                    else:
                        if line[3] not in symtab_reg:
                            errorFlag = True
                            error.update(flag = True, type = 'Invalid Register Specified', lineNo = lineNumber)
                            errorList.append(error)
                        else:
                            asdLine += addLeadingZeroes(bin(symtab_reg.get(line[3]))[2:], 3)
                            while len(asdLine) < 16:
                                asdLine += '0'
        
        assembled.append(asdLine)
        lineNumber += 1
        if extraLine is not '':
            assembled.append(extraLine)
            lineNumber += 1        
        ##print(assembled, '\n', errorList, '\n', errorFlag) 
    return lineNumber, assembled, errorList, errorFlag
                
        
        
        ##print(line) #testing #success