# Nathan Galdamez Gomez, 2141118
# This is ZyLab 9.10

# Use import csv module to read input1.csv
import csv

# Input the file for reading and creating a dictionary
my_file = open(input(), 'r')
info = csv.reader(my_file)
word_collection = dict()

# The nested for loop will read each word from the file and if their frequencies
for row in info:
    for word in row:
        if word in word_collection:
            word_collection[word] += + 1
        else:
            word_collection[word] = 1

