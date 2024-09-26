print ("Michael Mordec, 7/07/22, Lab 9, CSC 242:")

import random

# the Writer's Grid
grid = []
print ("grid line 1")
line1 = ["key", "medicine", "secretary", "beverage", "landscape"]
# line can be read from the CSV file
print (line1)
print ()
for item in line1 :
    grid.append(item)
print ("grid line 2")
# line can be read from the CSV file
line2 = ["village", "porch", "toy gun", "lamp", "telephone"]
print (line2)
print ()
for item in line2 :
    grid.append(item)

file = open("words.csv")
for line in file:
    for word in line.split(','):
        grid.append(word.strip())
file.close()

# randomly select a subset of elements ( the stack )
samples = random.sample(grid, 6)
# print (samples)
print ("[ the script ]")
print("")
print ("I started the day by looking for the", samples.pop(), end = ".")
print ()
print ("I planned later to walk to the", samples.pop(), end = ".")
print ()
print ("Surprisingly, I found the", samples.pop(), "was empty", end = ".")
print ()
print ("I wondered if a", samples.pop(), "would appear", end = ".")
print ()
print ("My aunt must have left my cellular telephone with the", samples.pop(), end = ".")
print ()
print ("Yesterday, I forgot to take the", samples.pop(), "to the meeting", end = ".")
print ("\n\n")

total_entropy = 0
print ("\n")
print ("please enter an integer that will describe the entropy analysis")
print ("for grid line 1")
entropy = int(input())
total_entropy += entropy
print ("estimated entropy for grid line 1:", entropy)
print ("for grid line 2")
entropy = int(input())
print ("estimated entropy for grid line 2:",  entropy)
total_entropy += entropy
print ("total entropy :",  total_entropy)
print ("\n\n")
