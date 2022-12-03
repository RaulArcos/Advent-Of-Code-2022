import os 

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)
elve = []
input = open("input.txt", 'r')
inputlines = input.readlines()
prioritysum = 0
for trio in grouper(inputlines,3):
    counter = 0
    for line in trio:
        elve.insert(counter,line)
        counter+1
    print(elve[0],elve[1],elve[2])
    for item in range(52):
        if(item < 26):
            if(chr(item+97) in elve[0] and chr(item+97) in elve[1] and chr(item+97) in elve[2]):
                prioritysum+=(item+1)
                print("En el trio coincide: ", chr(item+97),"(",item+1,")", ", La suma de prioridades es = ",prioritysum )
        else:
            if(chr(item+39) in elve[0] and chr(item+39) in elve[1] and chr(item+39) in elve[2]):
                prioritysum+=(item+1)
                print("En el trio coincide: ",chr(item+39),"(",item+1,")",", La suma de prioridades es = ",prioritysum )
    print("\n----------------------------------------------------------------------------------------------------------------")
print("\n\nLa suma final es = ",prioritysum)