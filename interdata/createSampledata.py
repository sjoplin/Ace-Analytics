# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import string


potOutcome = ["grounded", "flied", "lined", "double", "popped", "singled", "doubled", "tripled", "homered"]
direction = ['p', '3b.', 'catcher', 'shortstop', 'pitcher', '1b', 'first', '2b', 'c', 'second', '3b', 'third', 'ss', 'lf', 'left', 'cf', 'center', 'rf', 'right', 'down', 'middle', 'short']
trajectory = ['grounded', 'flied', 'lined']


names = [];
results = [];
area = [];
traj = [];
f = open('scraperaw.txt')
line = f.readline()

count = 0

while line:
    #print(line)

    words = line.split(' ')
    #print(words)
    #

    num = 0
    for each in potOutcome:

        if (each in words):
            #print(words)
            temp = words[words.index(each)]
            names.append(words[0].lower())
            results.append(temp.lower())

            num = 0;

            newlines = []
            for each in words:
                newlines.append(each.strip(','))
            words = newlines
            #print(words)

            for each in words:
                if (num == 0):
                    if (each in direction):
                        #print(words)
                        #if (num == 0):

                        #print(each)
                        count += 1
                                #print(count)
                        temp2 = words[words.index(each)]
                        area.append(temp2.lower())

                        num = 1






    line = f.readline()

f.close()

s = pd.Series(names)
p = pd.Series(results)
a = pd.Series(area)
data = pd.DataFrame({'Names':s, 'Results':p, 'Area':a})
pd.set_option('display.max_rows', 170)

print(data)
