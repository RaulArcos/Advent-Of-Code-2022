import numpy as np

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def crates_state(input):
    input = open(input, 'r')
    inputlines = input.readlines()
    
    for line in inputlines:
        line = line.split(' ')
        if(has_numbers(line) and line[0] != "move"):
            stacknum = int(line[-1-1])
    cratesrow = []
    crates = []
    for line in inputlines:
        
        if("move" not in line and line != '\n'):
            for space in line:


    print(crates)
        

        
           
            
                

            
def rearrangement_procedure(input):
    crates_state(input)



if '__main__' == __name__:
    print("Combinación final = ", rearrangement_procedure("inputtest.txt"))