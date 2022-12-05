def fullAsignmentCounter(input):
    input = open(input, 'r')
    inputlines = input.readlines()
    fullAsigCount = 0
    cont = 0
    for line in inputlines:
        cont +=1
        asigment = line.split(',')
        asigment = str(asigment).split('-')
        fullAsigCount = fullAsigCount+1 if ((int(asigment[0]) <= int(asigment[2]) and int(asigment[1]) >= int(asigment[3])) or (int(asigment[0]) >= int(asigment[2]) and int(asigment[1]) <= int(asigment[3]))) else fullAsigCount
    return fullAsigCount

if '__main__' == __name__:
    print(fullAsignmentCounter("input.txt"), "asignaciones completas encontradas.")