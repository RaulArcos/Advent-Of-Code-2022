
def fullAsignmentCounter(input):
    input = open(input, 'r')
    inputlines = input.readlines()
    fullAsigCount = 0
    for line in inputlines:
        line = line.split(',')
        first = line[0].split('-')
        second = line[1].split('-')
        fullAsigCount = fullAsigCount if(int(first[1])<int(second[0]) or int(second[1])<int(first[0])) else fullAsigCount+1
    return fullAsigCount

if '__main__' == __name__:
    print(fullAsignmentCounter("input.txt"), "asignaciones completas encontradas.")