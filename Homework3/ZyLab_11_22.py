# Nathan Galdamez Gomez, 2141118
# This is ZyLab 11.22

# words variable takes string input and splits inputted words into a variable called ws
words = str(input())
ws = words.split()

# The frequency of each word in ws will be counted in for loop
for w in ws:
    
    # freq is a variable that will hold each word's frequency
    freq = ws.count(w)
    
    #Print the word and its frequenccy
    print(w, freq)
