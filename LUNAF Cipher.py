'''
Caleb Ha
30/03/2023
LUNAF Cipher V1.1

This is the LUNAF Cipher. LUNAF is an acryonym for Layered Unbreakable Numerical Algorithm for Files.
This cipher is based upon a previous cipher I created, albeit slightly modified to work with files.
The TESS Cipher (Transformational Enhanced Shift System) used a modified version of the Ceaser Cipher which increases
the shift used as it encrypts the message. The LUNA Cipher is based on the same principle, however, it is over-encrypted with
a Polybius Square.

The LUNAF Cipher utilizes the principles of the LUNA Cipher, but is modified to take a 2 file names (input file & output file).
The LUNAF Cipher also doesn't support the transfer of the shift value embedded in the code, so the shift value must be communicated differently
if one wishes to decrypt a file.

Because of this, the LUNAF Cipher can take any positive integer value up to the maximum bite value.

1.0 (31/03/2023) -
Created the LUNAF Cipher with file encryption and decryption capabilities. No extra abilities

1.1 (03/04/2023)-
Added support for partial encryption by only using TESS
'''

# Encrypts the file using LUNA
def encryption(fileContents, shift, justTess=False, verbose=False):

    # 2D Array for the encrypted file
    encryptedFileContents = []

    # Contains the total shift
    numberShift = 0

    # Contains the line number
    lineNumber = 0

    # Loops through all the lines in the file
    for line in fileContents:

        # Adds a new list to the file
        encryptedFileContents.append([])

        # Loops through all the characters in the line
        for character in line:

            # Keeps track of the character
            i = 0

            # Finds the character in the character set
            while character != characterSet[i]:

                i += 1
            
            # Increases the number shift
            numberShift += shift

            # Increments the character
            i += numberShift

            # Makes i in the range of the length of the character set
            while i > len(characterSet) - 1:

                i -= len(characterSet)

            # Additional info
            if verbose:

                if character == "\n":

                    if characterSet[i] == "\n":

                        print(f"[Encryption :     TESS] Character: \\n, Shift: {numberShift}, Encrypted: \\n")
                
                    else:

                        print(f"[Encryption :     TESS] Character: \\n, Shift: {numberShift}, Encrypted: {characterSet[i]}")

                else:

                    print(f"[Encryption :     TESS] Character: {character}, Shift: {numberShift}, Encrypted: {characterSet[i]}")

            if justTess:            

                encryptedFileContents[lineNumber] += characterSet[i]

            elif not justTess:

                # Loops through all the rows in the polybius square            
                for row in range(len(polybiusSquare)):

                    # Loops through all the columns in the polybius square
                    for column in range(len(polybiusSquare[0])):

                        # Checks to see if the character is the same as the item in the list
                        if characterSet[i] == polybiusSquare[row][column]:

                            # Additional info
                            #! All if statemnts pass this are purely for if the any characters are \n
                            if verbose:

                                if characterSet[i] == "\n":

                                    print(f"[Encryption : Polybius] Character: \\n, Row: {row}, Column: {column}, Encrypted: {rowEncryptionCharacters[row] + columnEncryptionCharacters[column]}")
                                
                                else:

                                    print(f"[Encryption : Polybius] Character: {characterSet[i]}, Row: {row}, Column: {column}, Encrypted: {rowEncryptionCharacters[row] + columnEncryptionCharacters[column]}")

                            # Adds the encrypted character to the encrypted file contents list in the specific line
                            encryptedFileContents[lineNumber] += rowEncryptionCharacters[row] + columnEncryptionCharacters[column]
            
        # Increments the line number at the end of the loop
        lineNumber += 1

    # Returns the final encrypted phrase
    return encryptedFileContents

# Decrypts using Polybius Cipher
def decryptionPolybius(fileContents, verbose=False):

    # Contains the decrypted phrase
    decryptedContent = ""

    # Loops to iterate through all the characters (+1 to ensure that the try-except block is ran)
    for i in range(0, len(fileContents) + 1, 2):

        # Checks to see if the fileContents[i] is out of the index
        try:

            fileContents[i]
    
        # Runs at the end of the characters
        except IndexError:

            # Returns the decypted phrase
            return decryptedContent

        # Creates the encypted block
        encryptedBlock = fileContents[i] + fileContents[i + 1]

        # Loops through the all the characters in polybius square row string
        for row in range(len(polybiusSquare)):

            # Finds the row of the character
            if rowEncryptionCharacters[row] == encryptedBlock[0]:

                # Loops through all the characters in the polybius square column string
                for column in range(len(polybiusSquare[0])):

                    # Finds the column of the character
                    if columnEncryptionCharacters[column] == encryptedBlock[1]:

                        # Adds the decrypted character to the decrypted phrase
                        decryptedContent += polybiusSquare[row][column]

                        # Additional info
                        #! All if statemnts pass this are purely for if the any characters are \n
                        if verbose:


                            if polybiusSquare[row][column] == "\n":

                                print(f"[Decryption : Polybius] Encrypted: {encryptedBlock}, Row: {row}, Column: {column}, Decrypted: \\n")
                            
                            else:

                                print(f"[Decryption : Polybius] Encrypted: {encryptedBlock}, Row: {row}, Column: {column}, Decrypted: {polybiusSquare[row][column]}")

# Decrypts using TESS
def decryptionTess(fileContents, shift, verbose=False):

    # Contains the decrypted contents
    decryptedContents = ""

    # Contains the total shift value
    numberShift = 0

    # Loops through each character in the file
    for character in fileContents:

        i = 0

        # Finds the character in the character set
        while character != characterSet[i]:

            i += 1

        # Increases the total shift
        numberShift += shift

        # Decrements the character
        i -= numberShift

        # Ensures that the character is withing range of the character set
        while i < 0:

            i += len(characterSet)

        # Adds the decrypted character to the decrypted contents
        decryptedContents += characterSet[i]

        # Additional info
        #! All if statemnts pass this are purely for if the any characters are \n
        if verbose:

            if character == "\n":

                if characterSet[i] == "\n":

                    print(f"[Decryption :     TESS] Encrypted: \\n, Shift: {numberShift}, Decrypted Character: \\n")

                else:

                    print(f"[Decryption :     TESS] Encrypted: \\n, Shift: {numberShift}, Decrypted Character: {characterSet[i]}")

            else:
                
                if characterSet[i] == "\n":

                    print(f"[Decryption :     TESS] Encrypted: {character}, Shift: {numberShift}, Decrypted Character: \\n")

                else:

                    print(f"[Decryption :     TESS] Encrypted: {character}, Shift: {numberShift}, Decrypted Character: {characterSet[i]}")


    # Returns the decrypted contents
    return decryptedContents

# A list of 96 characters, organized in the order on a keyboard
characterSet = [
    '`', '~', '1', '!', '2', '@', '3', '#', '4', '$', '5', '%', '6', '^', '7', '&', '8', '*', '9', '(', '0', ')', '-', '_', '=', '+',
    'q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', '[', '{', ']', '}', 
    'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', ';', ':', '\'', '\"', '\\', '|', 
    'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', ',', '<', '.', '>', '/', '?',
    ' ', '\n'
]

# A 8x12 Polybius Square (Rectangle)
polybiusSquare = [

#     0    1    2    3    4    5    6    7
    ['`', '~', '1', '!', '2', '@', '3', '#'], # 0
    ['4', '$', '5', '%', '6', '^', '7', '&'], # 1
    ['8', '*', '9', '(', '0', ')', '-', '_'], # 2
    ['=', '+', 'q', 'Q', 'w', 'W', 'e', 'E'], # 3
    ['r', 'R', 't', 'T', 'y', 'Y', 'u', 'U'], # 4
    ['i', 'I', 'o', 'O', 'p', 'P', '[', '{'], # 5
    [']', '}', 'a', 'A', 's', 'S', 'd', 'D'], # 6
    ['f', 'F', 'g', 'G', 'h', 'H', 'j', 'J'], # 7
    ['k', 'K', 'l', 'L', ';', ':', '\'', '\"'], # 8
    ['\\', '|', 'z', 'Z', 'x', 'X', 'c', 'C'], # 9
    ['v', 'V', 'b', 'B', 'n', 'N', 'm', 'M'], # A
    [',', '<', '.', '>', '/', '?', ' ', '\n'] # B
]

# Holders of the characters used to encode the polybius square
rowEncryptionCharacters = "0123456789AB"
columnEncryptionCharacters = "01234567"

# Gets if the user wants to encrypt or decrypt a file
encryptOrDecrypt = input("Encrypt or decrypt? (e/d): ")

# Gets if the file should be encrypted or decrypted with just TESS of fully
justTess = input("TESS or Full Encryption? (t/f): ")

if justTess == "t":

    justTess = True

elif justTess == "f":

    justTess = False

# Gets the file name
fileName = input("Input file name: ")

# Gets the name for the new file
newFileName = input("New file name: ")

# Gets the shift value
shift = int(input("Input shift: "))

# Gets if the user wants to print verbose
verbose = input("Verbose? (y/n): ")

# Gets if the user wants to print additional info
if verbose == "y":

    verbose = True

# Option for encrypting
if encryptOrDecrypt == 'e':

    # Opens the file given
    with open(fileName, 'r') as file:

        # Grabs the file contents
        fileContents = file.readlines()
        
        # Makes a 2D list of the encrypted contents of a the file
        encryptedFileContents = encryption(fileContents, shift, justTess, verbose)

    # Opens a new file in append mode
    with open(newFileName, 'w') as encryptedFile:

        # Keeps a string of the encrypted characters
        encrypted = ""

        # Loops through all the encrypted lines
        for line in encryptedFileContents:

            # Loops through all the characters in the line
            for character in line:

                # Adds the encrypted character to encrypted
                encrypted += character

        # Writes the encrypted file contents
        encryptedFile.write(encrypted)

# Option for decrypting
elif encryptOrDecrypt == 'd':

    # Opens the encrypted file
    with open(fileName, 'r') as file:

        # Grabs the file contents
        fileContents = file.read()

    # Runs if the file contents is just encrypted with TESS
    if justTess:

        # Decrypts the file contents using TESS
        decrypted = decryptionTess(fileContents, shift, verbose)

        # Opens the decrypted file
        with open(newFileName, 'w') as decryptedFile:

            # Writes the decrypted contents to the decrypted file
            decryptedFile.write(decrypted)
    
    # Runs if the file contents are fully encrypted
    else:

        # Decrypts the file contents using the Polybius Square
        decryptedStep1 = decryptionPolybius(fileContents, verbose)

        # Decypts using TESS
        decryptedStep2 = decryptionTess(decryptedStep1, shift, verbose)

        # Opens the decrypted file
        with open(newFileName, 'w') as decryptedFile:

            # Writes the decrypted contents to the decrypted file
            decryptedFile.write(decryptedStep2)