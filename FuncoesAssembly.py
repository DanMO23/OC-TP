import sys

def funcoesSemParametro(arq_inst):
    
    for i in range(0, len(arq_inst)):
        if (arq_inst[i][0] == "\n" or arq_inst[i][0:1] == " \n"):
            continue
        else:
            if (arq_inst[i][0:4] == "bne "):
                opcode = OpBne(arq_inst[i])
            elif (arq_inst[i][0:3] == "sw "):
                opcode = OpSw(arq_inst[i])
            elif (arq_inst[i][0:4] == "addi"):
                opcode = OpAddi(arq_inst[i])
            elif (arq_inst[i][0:3] == "lw "):
                opcode = OpLw(arq_inst[i])
            elif (arq_inst[i][0:4] == "sll "):
                opcode = OpSll(arq_inst[i])
            elif (arq_inst[i][0:4] == "add "):
                opcode = OpAdd(arq_inst[i])
            elif (arq_inst[i][0:4] == "xor "):
                opcode = OpXor(arq_inst[i])
            else:
                opcode = "Instrução não localizada."
        print(opcode)
def funcoesComParametro(arq_inst, saida):
    for i in range(0, len(arq_inst)):
        if (arq_inst[i][0:4] == "bne "):
            opcode = OpBne(arq_inst[i])
        elif (arq_inst[i][0:3] == "sw "):
            opcode = OpSw(arq_inst[i])
        elif (arq_inst[i][0:4] == "addi"):
            opcode = OpAddi(arq_inst[i])
        elif (arq_inst[i][0:3] == "lw "):
            opcode = OpLw(arq_inst[i])
        elif (arq_inst[i][0:4] == "sll "):
            opcode = OpSll(arq_inst[i])
        elif (arq_inst[i][0:4] == "add "):
            opcode = OpAdd(arq_inst[i])
        elif (arq_inst[i][0:4] == "xor "):
            opcode = OpXor(arq_inst[i])
        else:
            opcode = "Instrução não localizada."
        if (i == 0):
            arqsaida = open(saida, "w")
        else:
            arqsaida = open(saida, "a")
        if (i == len(arq_inst)):
            arqsaida.write(opcode)
        else:
            arqsaida.write(str(opcode) + "\n")
        arqsaida.close
def OpBne(arq_inst):
    j, rs2, rs1, immediate = 5, '', '', ''
    while (arq_inst[j] != ','):
        rs1 = rs1 + arq_inst[j]
        j += 1
    j += 3
    while (arq_inst[j] != ','):
        rs2 = rs2 + arq_inst[j]
        j += 1
    j += 2
    while (j != len(arq_inst)):
        immediate = immediate + arq_inst[j]
        j += 1
    rs2 = int(rs2)
    rs2 = "{0:05b}".format(rs2)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    immediate = int(immediate)
    immediate = "{0:012b}".format(immediate)
    opcode = immediate[0:7] + rs2 + rs1 + "001" + immediate[7:12] + "1100011"
    return opcode
def OpSw(arq_inst):
    j, rs2, rs1, immediate = 4, '', '', ''
    while (arq_inst[j] != ','):
        rs2 = rs2 + arq_inst[j]
        j += 1
    j += 2
    while (arq_inst[j] != '('):
        immediate = immediate + arq_inst[j]
        j += 1
    j += 2
    while (arq_inst[j] != ')'):
        rs1 = rs1 + arq_inst[j]
        j += 1
    rs2 = int(rs2)
    rs2 = "{0:05b}".format(rs2)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    immediate = int(immediate)
    immediate = "{0:012b}".format(immediate)
    opcode = immediate[0:7] + rs2 + rs1 + "001" + immediate[7:12] + "0100011"
    return opcode
def OpAddi(arq_inst):
    j, rd, rs1, immediate = 6, '', '', ''
    while (arq_inst[j] != ','):
        rd = rd + arq_inst[j]
        j += 1
    j += 3
    while (arq_inst[j] != ','):
        rs1 = rs1 + arq_inst[j]
        j += 1
    j += 2
    if (arq_inst[j] == '-'):
        negativo = True
        j += 1
    while (j != len(arq_inst)):
        immediate = immediate + arq_inst[j]
        j += 1
    rd = int(rd)
    rd = "{0:05b}".format(rd)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    immediate = int(immediate)
    if (negativo):
        immediate = (pow(2, 12) - immediate)
        negativo = False
    immediate = "{0:012b}".format(immediate)
    opcode = immediate + rs1 + "000" + rd + "0010011"
    return opcode
def OpLw(arq_inst):
    j, rd, rs1, immediate = 4, '', '', ''
    while (arq_inst[j] != ','):
        rd = rd + arq_inst[j]
        j += 1
    j += 2
    while (arq_inst[j] != '('):
        immediate = immediate + arq_inst[j]
        j += 1
    j += 2
    while (arq_inst[j] != ')'):
        rs1 = rs1 + arq_inst[j]
        j += 1
    rd = int(rd)
    rd = "{0:05b}".format(rd)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    immediate = int(immediate)
    immediate = "{0:012b}".format(immediate)
    opcode = immediate + rs1 + "010" + rd + "0000011"
    return opcode
def OpSll(arq_inst):
    j, rd, rs1, rs2 = 5, '', '', ''
    while (arq_inst[j] != ','):
        rd = rd + arq_inst[j]
        j += 1
    j += 3
    while (arq_inst[j] != ','):
        rs1 = rs1 + arq_inst[j]
        j += 1
    j += 3
    while (j != len(arq_inst)):
        rs2 = rs2 + arq_inst[j]
        j += 1
    rd = int(rd)
    rd = "{0:05b}".format(rd)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    rs2 = int(rs2)
    rs2 = "{0:05b}".format(rs2)
    opcode = "0000000" + rs2 + rs1 + "001" + rd + "0110011"
    return opcode
def OpAdd(arq_inst):
    j, rd, rs1, rs2 = 5, '', '', ''
    while (arq_inst[j] != ','):
        rd = rd + arq_inst[j]
        j += 1
    j += 3
    while (arq_inst[j] != ','):
        rs1 = rs1 + arq_inst[j]
        j += 1
    j += 3
    while (j != len(arq_inst)):
        rs2 = rs2 + arq_inst[j]
        j += 1
    rd = int(rd)
    rd = "{0:05b}".format(rd)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    rs2 = int(rs2)
    rs2 = "{0:05b}".format(rs2)
    opcode = "0000000" + rs2 + rs1 + "000" + rd + "0110011"
    return opcode
def OpXor(arq_inst):
    j, rd, rs1, rs2 = 5, '', '', ''
    while (arq_inst[j] != ','):
        rd = rd + arq_inst[j]
        j += 1
    j += 3
    while (arq_inst[j] != ','):
        rs1 = rs1 + arq_inst[j]
        j += 1
    j += 3
    while (j != len(arq_inst)):
        rs2 = rs2 + arq_inst[j]
        j += 1
    rd = int(rd)
    rd = "{0:05b}".format(rd)
    rs1 = int(rs1)
    rs1 = "{0:05b}".format(rs1)
    rs2 = int(rs2)
    rs2 = "{0:05b}".format(rs2)
    opcode = "0000000" + rs2 + rs1 + "100" + rd + "0110011"
    return opcode
