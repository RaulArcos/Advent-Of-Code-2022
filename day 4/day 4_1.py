
def fullAsignmentCounter(input):
    input = open(input, 'r')
    inputlines = input.readlines()
    fullAsigCount = 0
    for line in inputlines:
        line = line.split(',')
        first = line[0].split('-')
        second = line[1].split('-')
        fullAsigCount = fullAsigCount+1 if (( int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or (int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]))) else fullAsigCount
    return fullAsigCount

if '__main__' == __name__:
    print(fullAsignmentCounter("input.txt"), "asignaciones completas encontradas.")