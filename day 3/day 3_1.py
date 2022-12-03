import os 
input = open("input.txt", 'r')
inputlines = input.readlines()
prioritysum = 0
for line in inputlines:
    if line != '\n':
        ruckSack1 = line[:len(line)//2]
        ruckSack2 = line[len(line)//2:]
        for item in range(52):
            if(item < 26):
                if(chr(item+97) in ruckSack1 and chr(item+97) in ruckSack2):
                    prioritysum+=(item+1)
                    print("Aquí coincide: ", chr(item+97),"(",item+1,")", ", La suma de prioridades es = ",prioritysum )
            else:
                if(chr(item+39) in ruckSack1 and chr(item+39) in ruckSack2):
                    prioritysum+=(item+1)
                    print("Aquí coincide: ",chr(item+39),"(",item+1,")",", La suma de prioridades es = ",prioritysum )
print("\n\nLa suma final es = ",prioritysum)