def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def get_num_columns(inputlines):  
    for line in inputlines:
        line = line.split(' ')
        if(has_numbers(line) and line[0] != "move"):
            stacknum = int(line[-1-1])
    return stacknum

def get_num_rows(inputlines):
    rows = 0
    for line in inputlines:
        if("move" not in line and not has_numbers(line) and line!="\n"):
            rows+=1
    return rows

def crates_state(input):
    input = open(input, 'r')
    inputlines = input.readlines()
    cratesrow = []
    crates = []
    cratesinv = []
   

    stacknum = get_num_columns(inputlines)
    altnum = get_num_rows(inputlines)

    for line in inputlines:
        cont = 0
        line = line.replace('[', '')
        line = line.replace(']', '')
        if("move" not in line and not has_numbers(line) and line!="\n"):
            for space in line:
                if(space == " "):
                    cont+=1
                else:
                    cont = 0
                    cratesrow.append(space)
                if(cont >=4):
                    cratesrow.append('0')
                    cont = 0
            crates.append(cratesrow)
            cratesrow = []
    for x in range(stacknum):
        y = altnum-1
        while y >= 0:
            cratesrow.append(crates[y][x])
            y-=1
        cratesinv.append(cratesrow)
        cratesrow = []
    print(cratesinv)
    return cratesinv    
            
def rearrangement_procedure(input):
    solution = []
    crates = crates_state(input)
    input = open(input, 'r')
    inputlines = input.readlines()
    for line in inputlines:
        line = line.split(" ")
        if("move" in line):
            print(line)
            for x in range(int(line[1])):
                n = get_num_rows(inputlines)-1
                while(n >= 0):
                    if(crates[(int(line[3])-1)][n] != 0):
                        crates[(int(line[5])-1)][n] = crates[(int(line[3])-1)][n]
                        crates[(int(line[3])-1)][n] = 0
                        n = -1
                    else:
                        n-=1
                
    for x in crates:
        solution.append(crates[x][0])
    return solution

if '__main__' == __name__:
    print("Combinación final = ", rearrangement_procedure("inputtest.txt"))