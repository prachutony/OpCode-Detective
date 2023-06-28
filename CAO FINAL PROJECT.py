import re
import difflib
opcode_list = ['ADD','ASSUME','ADC','CMP','DIV','DAS','DB','DD','DT','DQ','DW','EXTRN','ENDP','EVEN','EQU','GLOBAL',
               'HLT','INC','IN','INCLUDE','JUMP','LOAD','LABEL','LENGTH','MUL','MOV','NAME','OUT','ORG','OFFSET',
               'PPUSH','PTR','POP','POPF','PROC','PUSHF','PUBLIC','PUSHA','SAHF','SUB','STORE','SHORT','SEGMENT',
               'SBB','TYPE','CLI','STI','STC','CLC','CMC','STD','CLD','SCASW','CMPSW','LODSW','STOSW','MOVSW',
               'RET','CALL','LOOPNZ','LOOPZ','LOOP','JCXZ','JNO','JO','JPO','JPE','JNS','JS','JNZ','JZ','JNG',
               'RCL','RCR','ROL','SAL','SHL','SAR','SHR',]

opcode_list.sort()

def closest_match(search_string, string_list):
    closest_match = difflib.get_close_matches(search_string, string_list, n=1,cutoff =  0.65)
    if closest_match:
        return closest_match[0]
    else:
        return 0

def no_match(word , word_list):
    count = 0
    for i in range(len(word)):
        for j in range(len(word_list)):
            if word[i] not in word_list[j]:
                count += 1
    if count == len(word)*len(word_list):
        return 1
    else:
        return 0
        
code = []
print("Write your code here and to finish the code ENTER 2 times:")
while True:
    input_code = input()

    if input_code == '':
        break
    else:
        code.append(input_code.upper())
        

symbol_list = ["START" , "END"]
for i in range(len(code)):#This loop spilts the START and END , and also delete the whitespaces in the line
    if ":" in code[i]:
        if code[i].split(':')[0].strip() not in symbol_list:
            new_word_1 = closest_match(code[i].split(':')[0].strip(),symbol_list)
            print(new_word_1 , i+1)
            print(f'Error at line {i+1}: Did you mean "{new_word_1}"?')
        code[i] = code[i].split(':')[1].strip()
    else:
        code[i] = code[i].strip()
for i in range(len(code)):#This loop spilts each word in the line
    code[i] = code[i].split(' ')



try:
    for i in range(len(code)):#main loop
        for j in range(len(code)):
            if code[i][0] not in opcode_list:
                check = no_match(code[i][0].upper(),opcode_list)
                if check == 0:
                    new_word = closest_match(code[i][0],opcode_list)
                    if new_word == 0:
                        print(f'Error at line {i+1}: Unknown opcode "{code[i][0]}",There is no opcode like "{code[i][0]}".')
                        break
                    else:
                        print(f'Error at line {i+1}: Unknown opcode "{code[i][0]}",Did you mean "{new_word}"?')
                        break
                else:
                    print(f'Error at line {i+1}: Unknown opcode "{code[i][0]}",There is no opcode like "{code[i][0]}".')
                    break
except IndexError:
    pass
