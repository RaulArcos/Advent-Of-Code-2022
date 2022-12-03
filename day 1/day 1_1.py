import os 
input = open("input.txt", "r")
inputlines = input.readlines()
maxelve= 0
sum_newelve = 0 
for line in inputlines:
    if line != '\n':
        sum_newelve += int(line) 
        if(sum_newelve > maxelve):
            maxelve = sum_newelve
    else: 
        print("Actual max = ", maxelve)
        sum_newelve = 0
print("Max Cal Elve = ", maxelve)