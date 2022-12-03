import os 
input = open("input.txt", 'r')
inputlines = input.readlines()
top1elve = 0
top2elve = 0
top3elve = 0
sum_newelve = 0 
for line in inputlines:
    if line != '\n':
        sum_newelve += int(line) 
    else: 
        if(sum_newelve > top1elve):
            top3elve = top2elve
            top2elve = top1elve
            top1elve = sum_newelve
        if(sum_newelve > top2elve and sum_newelve < top1elve):
            top3elve = top2elve
            top2elve = sum_newelve
        if(sum_newelve > top3elve and sum_newelve < top2elve):
            top3elve = sum_newelve
        print("Actual TOP1 = ", top1elve)
        print("Actual TOP2 = ", top2elve)
        print("Actual TOP3 = ", top3elve)
        sum_newelve = 0


print("Max Cal TOP 3 ElveS = ", top2elve+top1elve+top3elve)