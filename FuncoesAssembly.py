import sys

Opcode = {
    'R':"0110011",
    'I':"0000011",
    'S':"0100011",
    'SB':"1100011"
    }

func3 = {
    'add':"000",
    'xor':"100",
    'sll':"001"
}

func7 ={
    'add':"0000000",
    'xor':"0000000",
    'sll':"0000000"

}



def funcoesSemParametro(arq_inst):
    
    for i in range(0, len(arq_inst)):
        if (arq_inst[i][0] == "\n" or arq_inst[i][0:1] == " \n"):
            continue
        else:
            assemblyBin = DefinirInstrução(arq_inst, i)
        print(assemblyBin)
def funcoesComParametro(arq_inst, saida):
    for i in range(0, len(arq_inst)):
        if (arq_inst[i][0] == "\n" or arq_inst[i][0:1] == " \n"):
            continue
        else:
            assemblyBin = DefinirInstrução(arq_inst, i)


            if (i == 0):
                arqsaida = open(saida, "w")
            else:
                arqsaida = open(saida, "a")
            if (i == len(arq_inst)):
                arqsaida.write(assemblyBin)
            else:
                arqsaida.write(str(assemblyBin) + "\n")
            arqsaida.close


def DefinirInstrução(arq_inst, i):
    
    if (arq_inst[i][0:4] == "bne "):
        assemblyBin = OpBne(arq_inst[i])
    elif (arq_inst[i][0:3] == "sw "):
        assemblyBin = OpSw(arq_inst[i])
    elif (arq_inst[i][0:4] == "addi"):
        assemblyBin = OpAddi(arq_inst[i])
    elif (arq_inst[i][0:3] == "lw "):
        assemblyBin = OpLw(arq_inst[i])
    elif (arq_inst[i][0:4] == "sll "):
        assemblyBin = OpSll(arq_inst[i])
    elif (arq_inst[i][0:4] == "add "):
        assemblyBin = OpAdd(arq_inst[i])
    elif (arq_inst[i][0:4] == "xor "):
        assemblyBin = OpXor(arq_inst[i])
    else:
        assemblyBin = "Instrução não localizada."

    return assemblyBin


        


def FormatR(arq_inst, func3, func7):
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
    assemblyBin = func7 + rs2 + rs1 + func3 + rd + Opcode["R"]
    
    return assemblyBin





#Bne - Instrução no formato SB
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
    assemblyBin = immediate[0:7] + rs2 + rs1 + "001" + immediate[7:12] + "1100011"
    return assemblyBin

#Sw - Instrução no formato S
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
    assemblyBin = immediate[0:7] + rs2 + rs1 + "001" + immediate[7:12] + "0100011"
    return assemblyBin

#Addi - Instrução no formato I
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
    assemblyBin = immediate + rs1 + "000" + rd + "0010011"
    return assemblyBin

#Lw - Instrução no formato I
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
    assemblyBin = immediate + rs1 + "010" + rd + "0000011"
    return assemblyBin

#Sll - Instrução no formato R
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
    assemblyBin = "0000000" + rs2 + rs1 + "001" + rd + "0110011"
    return assemblyBin

#Add - Instrução no formato R
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
    assemblyBin = "0000000" + rs2 + rs1 + "000" + rd + Opcode['R']
    return assemblyBin

#Xor - Instrução no formato R
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
    assemblyBin = "0000000" + rs2 + rs1 + "100" + rd + "0110011"
    return assemblyBin
