# ceaser cypher for text data

inputText = input("Enter your text: ")

asciiValues = []
outputText = ""
for char in inputText:
    asciiValues.append(ord(char))

A, a, Z, z = ord("A"), ord("a"), ord("Z"), ord("z")

shift = int(input("Enter how many shift to be done"))

for asciiValue in asciiValues:
    if shift >=24:
        shift %=24

    # for captial letters
    if(A <= asciiValue <= Z):
        if(asciiValue + shift > Z):
            asciiValue = A + (asciiValue + shift - Z) - 1
        
        else:
            asciiValue += shift

    # for small letters
    elif(a <= asciiValue <= z):
        if(asciiValue + shift > z):
            asciiValue = a + (asciiValue + shift - z) - 1
        
        else:
            asciiValue += shift

    outputText += chr(asciiValue)

print(outputText)