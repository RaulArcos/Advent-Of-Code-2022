def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def crates_state(input):
    input = open(input, 'r')
    inputlines = input.readlines()
    crates = []
    stacknum = 0

    for line in inputlines:
        line = line.split(' ')
        if(has_numbers(line) and line[0] != "move"):
            stacknum = int(line[-1-1])
    for line in inputlines:
        line = line.split(' ')
        print(line)
        

        
           
            
                

            
def rearrangement_procedure(input):
    crates_state(input)



if '__main__' == __name__:
    print("Combinación final = ", rearrangement_procedure("inputtest.txt"))