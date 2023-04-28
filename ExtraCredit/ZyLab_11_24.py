# Nathan Galdamez Gomez, 2141118
# This is ZyLab 11.24

# Both sentences are taken as input that will be in two lists of strings
sentence_1 = str(input()).split()
sentence_2 = str(input()).split()

# for loop will search each element inside the list
for i in range(len(sentence_1)):

    # The if statement below will print word pairs for inputs that differ between the two sentences
    if sentence_1[i] != sentence_2[i]:
        print(f'{sentence_1[i]} {sentence_2[i]}')
        