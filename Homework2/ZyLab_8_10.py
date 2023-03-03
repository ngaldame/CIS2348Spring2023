# Nathan Galdamez Gomez, 2141118
def palindrome(a):
    b = a.replace(' ', '')
    return b == b[::-1]


# Get input and store input in the drome variable that will call the palindrome function for the input
word = str(input())
drome = palindrome(word)

# Test if input is a palindrome or not
if drome:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')